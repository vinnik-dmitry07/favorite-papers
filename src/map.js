/* Litmaps-style layout for the key-papers corpus.
   x = publication date, y = cited-by, outgoing cites, parent-only outgoing
   cites, unique nested outgoing cites, outgoing cites plus
   a 1/cited bonus per outgoing target, any of those cites modes plus
   cited-by, the Litmaps citation count, or the aggregated quality
   score (toggle). Circle size is in-list cited-by (Litmaps count on
   the citation-count axis). Colour can follow the topic or the
   aggregated quality score (−1 red, +1 green). Curved links =
   "this paper cites that one".
   Positions are data-driven; a collision pass only nudges overlapping
   nodes apart inside a per-node box. */
(function () {
  'use strict';

  var data = window.GRAPH_DATA;
  var MARGIN = { top: 74, right: 96, bottom: 62, left: 62 };
  var GUTTER = 132;          // parking band for entries with no known date
  var ZERO_BAND = 78;        // breathing room for zeros / missing y-values
  var LABEL_FONT = 10.5;
  var CITE_TICKS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000,
                    2000, 5000, 10000, 20000, 50000];
  var QUALITY_TICKS = [-1, -0.5, 0, 0.5, 1];
  var UNTAGGED = '#9aa3ab';
  var IDEA_STROKE = '#74838c';
  var QUALITY_FILL = d3.scaleLinear()
    .domain([-1, 0, 1])
    .range(['#c62828', '#d9d3c5', '#2e7d32'])
    .clamp(true);
  var taxonomy = data.taxonomy || { fields: [], ideas: [] };
  var TOPIC_COLOR = {};
  var FIELD_SET = {};
  (taxonomy.fields || []).forEach(function (field) {
    TOPIC_COLOR[field.id] = field.color;
    FIELD_SET[field.id] = true;
  });
  function topicColor(d) {
    return (d.topic && TOPIC_COLOR[d.topic]) || UNTAGGED;
  }

  function qualityColorOn() {
    var el = document.getElementById('qcolor');
    return Boolean(el && el.checked);
  }

  function qualityColor(q) {
    return QUALITY_FILL(q);
  }

  function nodeFill(d) {
    if (qualityColorOn()) {
      return d.quality == null ? UNTAGGED : qualityColor(d.quality);
    }
    return topicColor(d);
  }

  function nodeFillOpacity(d) {
    if (qualityColorOn() && d.quality == null) return 0.4;
    return hasY(d) ? 0.88 : 0.4;
  }

  function formatCount(n) {
    if (n == null) return null;
    if (n >= 100000) return String(Math.round(n / 1000)) + 'k';
    if (n >= 1000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return String(n);
  }

  function formatQuality(q) {
    if (q == null) return null;
    return (q > 0 ? '+' : '') + q.toFixed(2);
  }

  function formatQualityTick(v) {
    if (v === 0) return '0';
    var mag = Math.abs(v) === 1 ? '1' : Math.abs(v).toFixed(1);
    return (v > 0 ? '+' : '-') + mag;
  }

  var svg = d3.select('#map');
  var gAxes = svg.append('g');
  var gRoot = svg.append('g');
  var gEdges = gRoot.append('g').attr('class', 'edges');
  var gNodes = gRoot.append('g').attr('class', 'nodes');
  // Labels sit outside the zoom transform so they keep a constant size.
  var gLabels = svg.append('g').attr('class', 'labels');
  var tip = d3.select('#tip');

  var nodes = data.nodes.map(function (n, i) {
    return Object.assign({}, n, {
      index: i,
      time: n.date ? new Date(n.date + 'T00:00:00Z') : null,
      score: 0,
      tag: n.keyword || n.label,
      haystack: [n.keyword, n.label, n.title, n.entry, n.section, n.kind,
                 n.topic || '', (n.ideas || []).join(' '),
                 (n.tags || []).join(' '),
                 (n.authors || []).join(' '),
                 n.telegram ? 'telegram' : ''].join(' ').toLowerCase()
    });
  });
  var edges = data.edges.map(function (e) {
    return { source: nodes[e[0]], target: nodes[e[1]], evidence: e[2] };
  });

  var neighbours = nodes.map(function () { return { inc: [], out: [] }; });
  edges.forEach(function (e) {
    neighbours[e.source.index].out.push(e.target.index);
    neighbours[e.target.index].inc.push(e.source.index);
  });

  // Papers a citing-filter hit must point at. The seeds themselves stay visible.
  var SEED_IDS = {
    'arxiv:2407.21783': true,  // Llama 3
    'arxiv:2501.00656': true,  // OLMo 2
    'arxiv:2506.10947': true,  // Spurious Rewards
    'arxiv:2601.11061': true,  // Spurious Rewards Paradox
    'arxiv:2604.01754': true   // LiveMathematicianBench
  };
  var seedIndex = {};
  var citesSeed = {};
  nodes.forEach(function (d) {
    if (SEED_IDS[d.id]) {
      seedIndex[d.index] = true;
      citesSeed[d.index] = true;
    }
  });
  edges.forEach(function (e) {
    if (seedIndex[e.target.index]) citesSeed[e.source.index] = true;
  });

  // Parent / child is only about outgoing cites. If A cites B and C, and C
  // cites B, then B is the parent and C is the child.
  // parents: count B only.
  // children: every unique paper reachable by following outgoing cites
  // from A (nested, no repetitions).
  nodes.forEach(function (d) {
    var cited = neighbours[d.index].out;
    var citedSet = {};
    cited.forEach(function (i) { citedSet[i] = true; });
    d.parentRefs = cited.filter(function (i) {
      return !neighbours[i].out.some(function (j) { return citedSet[j]; });
    }).length;
    var seen = {};
    var queue = [];
    cited.forEach(function (i) {
      seen[i] = true;
      queue.push(i);
    });
    var head = 0;
    while (head < queue.length) {
      var cur = queue[head];
      head += 1;
      neighbours[cur].out.forEach(function (i) {
        if (i === d.index || seen[i]) return;
        seen[i] = true;
        queue.push(i);
      });
    }
    d.childRefs = Object.keys(seen).length;
  });

  // Bonus inversely proportional to how often the target is cited on this
  // list: citing T adds 1/cited(T). Exclusive cites still add a full +1.
  nodes.forEach(function (d) {
    d.bonusAmount = 0;
    neighbours[d.index].out.forEach(function (i) {
      var cited = neighbours[i].inc.length;
      if (cited) d.bonusAmount += 1 / cited;
    });
    d.bonusRefs = d.refs + d.bonusAmount;
  });

  var maxY = 1;
  var radius = d3.scaleSqrt().domain([0, 1]).range([4, 21]);
  // Exponent > 1 stretches the top of the log scale so the last few parents
  // are not stacked on one pixel row.
  var Y_STRETCH = 1.75;

  function yEncode(count) {
    if (count <= 0) return 0;
    var u = Math.log1p(count) / (Math.log1p(maxY) || 1);
    if (u < 0) u = 0;
    if (u > 1) u = 1;
    return Math.pow(u, Y_STRETCH);
  }

  function yMode() {
    var el = document.getElementById('yaxis');
    var value = el ? el.value : 'cited';
    if (value === 'cites' || value === 'parents' || value === 'children'
        || value === 'bonus' || value === 'citations' || value === 'quality') {
      return value;
    }
    return 'cited';
  }

  function qualityMode() {
    return yMode() === 'quality';
  }

  function citeModeOn() {
    var mode = yMode();
    return mode === 'cites' || mode === 'parents'
      || mode === 'children' || mode === 'bonus';
  }

  function addCitedOn() {
    var el = document.getElementById('addcited');
    return citeModeOn() && Boolean(el && el.checked);
  }

  function syncAddCited() {
    var wrap = document.getElementById('addcited-wrap');
    if (wrap) wrap.hidden = !citeModeOn();
  }

  function baseYCount(d) {
    if (yMode() === 'cites') return d.refs;
    if (yMode() === 'parents') return d.parentRefs;
    if (yMode() === 'children') return d.childRefs;
    if (yMode() === 'bonus') return d.bonusRefs;
    if (yMode() === 'citations') return d.lit_cites || 0;
    return d.cites;
  }

  function yCount(d) {
    var n = baseYCount(d);
    if (addCitedOn()) n += d.cites;
    return n;
  }

  function hasY(d) {
    if (qualityMode()) return d.quality != null;
    return yCount(d) > 0;
  }

  function yAxisCaption() {
    if (yMode() === 'cites') {
      return addCitedOn()
        ? '\u2192 more cited-by + cites on this list'
        : '\u2192 cites more papers on this list';
    }
    if (yMode() === 'parents') {
      return addCitedOn()
        ? '\u2192 more cited-by + parent cites on this list'
        : '\u2192 cites more parent papers on this list';
    }
    if (yMode() === 'children') {
      return addCitedOn()
        ? '\u2192 more cited-by + nested outgoing cites on this list'
        : '\u2192 more nested outgoing cites on this list';
    }
    if (yMode() === 'bonus') {
      return addCitedOn()
        ? '\u2192 more cited-by + cites, with a larger bonus for less-cited targets'
        : '\u2192 more cites, with a larger bonus for less-cited targets';
    }
    if (yMode() === 'citations') return '\u2192 more citations';
    if (yMode() === 'quality') return '\u2192 higher aggregated quality';
    return '\u2192 cited by more papers on this list';
  }

  function yNote() {
    if (yMode() === 'cites') {
      return addCitedOn()
        ? 'y: cited by plus outgoing cites on this list'
        : 'y: outgoing cites to other entries on this list';
    }
    if (yMode() === 'parents') {
      return (addCitedOn()
        ? 'y: cited by plus outgoing parent cites on this list '
        : 'y: outgoing parent cites on this list ')
        + '(child cite dropped when its parent is also cited)';
    }
    if (yMode() === 'children') {
      return addCitedOn()
        ? 'y: cited by plus unique nested outgoing cites on this list'
        : 'y: unique nested outgoing cites on this list';
    }
    if (yMode() === 'bonus') {
      return addCitedOn()
        ? 'y: cited by plus outgoing cites plus a 1/cited bonus for each target'
        : 'y: outgoing cites plus a 1/cited bonus for each target';
    }
    if (yMode() === 'citations') return 'y: Litmaps citation count';
    if (yMode() === 'quality') return 'y: aggregated quality score';
    return 'y: cited by other entries on this list';
  }

  function sizeValue(d) {
    if (yMode() === 'citations') return d.lit_cites || 0;
    return d.cites;
  }

  function applyMetric() {
    radius = d3.scaleSqrt()
      .domain([0, d3.max(nodes, sizeValue) || 1])
      .range([4, 21]);
    if (qualityMode()) {
      maxY = 1;
      nodes.forEach(function (d) {
        var q = d.quality;
        d.r = radius(sizeValue(d));
        d.score = (q == null ? 0 : q + 1) * 2 + (d.cites + d.refs) * 0.5;
      });
      return;
    }
    maxY = d3.max(nodes, yCount) || 1;
    nodes.forEach(function (d) {
      var yv = yCount(d);
      d.r = radius(sizeValue(d));
      d.score = yv * 2 + (d.cites + d.refs - yv) * 0.5;
    });
  }
  applyMetric();

  var xBase, yBase, transform = d3.zoomIdentity, plot = {};
  var hovered = null, locked = null, matches = null, tagFilter = null;
  var PREFS_KEY = 'key-papers-map-prefs';

  function optionExists(select, value) {
    for (var i = 0; i < select.options.length; i += 1) {
      if (select.options[i].value === value) return true;
    }
    return false;
  }

  function loadPrefs() {
    try {
      var raw = window.localStorage.getItem(PREFS_KEY);
      if (!raw) return {};
      var parsed = JSON.parse(raw);
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (err) {
      return {};
    }
  }

  function savePrefs() {
    try {
      window.localStorage.setItem(PREFS_KEY, JSON.stringify({
        labels: document.getElementById('labels').value,
        yaxis: document.getElementById('yaxis').value,
        addcited: document.getElementById('addcited').checked,
        edges: document.getElementById('edges').checked,
        citefilter: document.getElementById('citefilter').checked,
        tgfilter: document.getElementById('tgfilter').checked,
        qcolor: document.getElementById('qcolor').checked,
        tag: tagFilter
      }));
    } catch (err) {
      return;
    }
  }

  function applyPrefs() {
    var prefs = loadPrefs();
    var labels = document.getElementById('labels');
    if (prefs.labels && optionExists(labels, prefs.labels)) {
      labels.value = prefs.labels;
    }
    var yaxis = document.getElementById('yaxis');
    if (prefs.yaxis && optionExists(yaxis, prefs.yaxis)) {
      yaxis.value = prefs.yaxis;
    }
    if (typeof prefs.addcited === 'boolean') {
      document.getElementById('addcited').checked = prefs.addcited;
    }
    if (typeof prefs.edges === 'boolean') {
      document.getElementById('edges').checked = prefs.edges;
    }
    if (typeof prefs.citefilter === 'boolean') {
      document.getElementById('citefilter').checked = prefs.citefilter;
    }
    if (typeof prefs.tgfilter === 'boolean') {
      document.getElementById('tgfilter').checked = prefs.tgfilter;
    }
    if (typeof prefs.qcolor === 'boolean') {
      document.getElementById('qcolor').checked = prefs.qcolor;
    }
    if (prefs.tag === 'untagged' || (prefs.tag && nodes.some(function (d) {
      return (d.tags || []).indexOf(prefs.tag) >= 0;
    }))) {
      tagFilter = prefs.tag;
    }
  }

  function syncEdges() {
    gEdges.attr('display', document.getElementById('edges').checked ? null : 'none');
  }

  applyPrefs();

  var zoom = d3.zoom().scaleExtent([0.55, 9]).on('zoom', function (event) {
    transform = event.transform;
    gRoot.attr('transform', transform);
    redrawAxes();
    restyleForZoom();
    scheduleLabels();
  });
  svg.call(zoom).on('dblclick.zoom', null);

  function layout() {
    var box = svg.node().getBoundingClientRect();
    var header = document.querySelector('header').getBoundingClientRect();
    plot = {
      left: MARGIN.left,
      right: box.width - MARGIN.right,
      top: Math.max(MARGIN.top, header.height + 22),
      bottom: box.height - MARGIN.bottom,
      width: box.width,
      height: box.height
    };
    var timeLeft = plot.left + GUTTER + 30;
    var dates = nodes.filter(function (d) { return d.time; })
                     .map(function (d) { return d.time; });
    var span = [d3.min(dates), d3.max(dates)];
    var padMs = (span[1] - span[0]) * 0.035;

    xBase = d3.scaleTime()
      .domain([new Date(+span[0] - padMs), new Date(+span[1] + padMs)])
      .range([timeLeft, plot.right]);
    applyMetric();
    yBase = qualityMode()
      ? d3.scaleLinear()
          .domain([-1, 1])
          .range([plot.bottom - ZERO_BAND, plot.top + 72])
      : d3.scaleLinear()
          .domain([yEncode(1), 1])
          .range([plot.bottom - ZERO_BAND, plot.top + 72]);

    // Uncited / unscored entries would otherwise pile onto a single pixel row.
    plot.zeroLow = plot.bottom - 12;
    plot.zeroHigh = plot.bottom - ZERO_BAND + 16;
    plot.zeroRule = plot.bottom - ZERO_BAND + 6;

    var gutterMid = plot.left + GUTTER / 2;
    function yRow(v) {
      if (v <= 0) return plot.zeroRule;
      return yBase(yEncode(v));
    }
    function clampNudge(gap) {
      return Math.max(6, Math.min(24, 0.45 * gap));
    }
    function rowGap(fromY, yv, dir) {
      var step = 1;
      var gap = dir * (fromY - yRow(yv + dir * step));
      while (gap < 12 && step < 24) {
        step += 1;
        var next = yv + dir * step;
        if (dir < 0 && next <= 0) {
          gap = dir * (fromY - plot.zeroRule);
          break;
        }
        gap = dir * (fromY - yRow(next));
      }
      return gap;
    }
    nodes.forEach(function (d, i) {
      var wobble = ((i * 2654435761) % 1000) / 1000 - 0.5;
      d.tx = d.time ? xBase(d.time) : gutterMid + wobble * (GUTTER - 26);
      d.ty = hasY(d)
        ? (qualityMode() ? yBase(d.quality) : yBase(yEncode(yCount(d))))
          + wobble * 4
        : plot.zeroLow - (wobble + 0.5) * (plot.zeroLow - plot.zeroHigh);
      d.x = d.tx;
      d.y = d.ty;
      d.undated = !d.time;
      if (d.undated) {
        d.xLo = plot.left + d.r;
        d.xHi = plot.left + GUTTER - d.r;
      } else {
        var dxMax = Math.max(24, d.r * 2.2);
        d.xLo = Math.max(timeLeft - 14, d.tx - dxMax);
        d.xHi = Math.min(plot.right + 26, d.tx + dxMax);
      }
      var up = 6;
      var down = 10;
      if (hasY(d)) {
        if (qualityMode()) {
          up = 12;
          down = 12;
        } else {
          var yv = yCount(d);
          var near = Math.abs(d.ty - yRow(yv + 1)) < 12
            || Math.abs(yRow(yv - 1) - d.ty) < 12;
          if (near) {
            up = 20;
            down = 20;
          } else {
            up = clampNudge(rowGap(d.ty, yv, 1));
            down = clampNudge(rowGap(d.ty, yv, -1));
          }
        }
      }
      d.yLo = Math.max(plot.top, d.ty - up);
      d.yHi = Math.min(plot.bottom, d.ty + down);
    });

    var sim = d3.forceSimulation(nodes)
      .force('x', d3.forceX(function (d) { return d.tx; }).strength(0.3))
      .force('y', d3.forceY(function (d) { return d.ty; }).strength(0.35))
      .force('collide', d3.forceCollide(function (d) { return d.r + 1.2; })
                          .strength(0.9).iterations(5))
      .force('bounds', function () {
        nodes.forEach(function (d) {
          if (d.x < d.xLo) { d.x = d.xLo; d.vx = 0; }
          else if (d.x > d.xHi) { d.x = d.xHi; d.vx = 0; }
          if (d.y < d.yLo) { d.y = d.yLo; d.vy = 0; }
          else if (d.y > d.yHi) { d.y = d.yHi; d.vy = 0; }
        });
      })
      .stop();
    for (var t = 0; t < 300; t += 1) sim.tick();

    nodes.forEach(function (d) {
      d.y = Math.max(plot.top, Math.min(plot.bottom, d.y));
    });
    plot.timeLeft = timeLeft;
  }

  function edgePath(e) {
    var a = e.source, b = e.target;
    var dx = b.x - a.x, dy = b.y - a.y;
    var len = Math.hypot(dx, dy) || 1;
    var bow = Math.min(70, len * 0.15);
    var mx = (a.x + b.x) / 2 - (dy / len) * bow;
    var my = (a.y + b.y) / 2 + (dx / len) * bow;
    return 'M' + a.x + ',' + a.y + 'Q' + mx + ',' + my + ' ' + b.x + ',' + b.y;
  }

  function redrawAxes() {
    var x = transform.rescaleX(xBase);
    var y = transform.rescaleY(yBase);
    var quality = qualityMode();
    var ticks = quality
      ? QUALITY_TICKS
      : CITE_TICKS.filter(function (c) { return c <= maxY * 1.3; });
    var tickAt = function (c) { return quality ? y(c) : y(yEncode(c)); };
    gAxes.selectAll('*').remove();

    gAxes.append('g')
      .attr('class', 'grid')
      .selectAll('line')
      .data(ticks)
      .join('line')
      .attr('x1', plot.timeLeft - 22).attr('x2', plot.right)
      .attr('y1', tickAt)
      .attr('y2', tickAt);

    gAxes.append('g')
      .attr('class', 'axis')
      .attr('transform', 'translate(0,' + plot.bottom + ')')
      .call(d3.axisBottom(x).ticks(Math.max(4, Math.round(plot.width / 150))))
      .call(function (g) { g.select('.domain').remove(); });

    gAxes.append('g')
      .attr('class', 'axis')
      .attr('transform', 'translate(' + (plot.timeLeft - 22) + ',0)')
      .call(d3.axisLeft(y)
        .tickValues(quality ? ticks : ticks.map(yEncode))
        .tickFormat(function (v, i) {
          return quality ? formatQualityTick(ticks[i]) : formatCount(ticks[i]);
        }))
      .call(function (g) { g.select('.domain').remove(); });

    gAxes.append('line')
      .attr('class', 'gutter-rule')
      .attr('x1', plot.timeLeft - 22).attr('x2', plot.right)
      .attr('y1', transform.applyY(plot.zeroRule))
      .attr('y2', transform.applyY(plot.zeroRule));

    gAxes.append('text')
      .attr('class', 'zero-band')
      .attr('text-anchor', 'end')
      .attr('fill', 'var(--muted)')
      .attr('font-size', 11)
      .attr('x', plot.timeLeft - 27)
      .attr('y', transform.applyY((plot.zeroLow + plot.zeroHigh) / 2) + 4)
      .text(qualityMode() ? 'n/a' : '0');

    gAxes.append('text')
      .attr('class', 'caption')
      .attr('text-anchor', 'middle')
      .attr('x', (plot.timeLeft + plot.right) / 2)
      .attr('y', plot.bottom + 42)
      .text('more recently published \u2192');

    gAxes.append('text')
      .attr('class', 'caption')
      .attr('transform', 'translate(' + (plot.right + 44) + ','
        + (plot.top + plot.bottom) / 2 + ') rotate(-90)')
      .attr('text-anchor', 'middle')
      .text(yAxisCaption());

    // The gutter holds real nodes, so it has to travel with the zoom.
    var gutterEnd = transform.applyX(plot.left + GUTTER + 12);
    gAxes.append('line')
      .attr('class', 'gutter-rule')
      .attr('x1', gutterEnd).attr('x2', gutterEnd)
      .attr('y1', plot.top - 12).attr('y2', plot.bottom);

    gAxes.append('text')
      .attr('class', 'caption')
      .attr('text-anchor', 'middle')
      .attr('x', transform.applyX(plot.left + GUTTER / 2))
      .attr('y', plot.bottom + 18)
      .text('date unknown');
  }

  var nodeSel, edgeSel, labelSel;

  function render() {
    edgeSel = gEdges.selectAll('path').data(edges).join('path')
      .attr('class', 'edge')
      .attr('stroke', 'var(--edge)')
      .attr('d', edgePath);

    nodeSel = gNodes.selectAll('g').data(nodes).join('g')
      .attr('class', 'node')
      .attr('transform', function (d) {
        return 'translate(' + d.x + ',' + d.y + ')';
      });
    nodeSel.selectAll('circle').data(function (d) { return [d]; }).join('circle')
      .attr('r', function (d) { return d.r; })
      .attr('fill', nodeFill)
      .attr('stroke', '#fff')
      .attr('fill-opacity', nodeFillOpacity)
      .on('mouseenter', function (event, d) { enter(d, event); })
      .on('mousemove', function (event) { if (!locked) moveTip(event); })
      .on('mouseleave', leave)
      .on('click', onClick)
      .on('dblclick', onDblClick);

    labelSel = gLabels.selectAll('text').data(nodes).join('text')
      .attr('class', 'label')
      .attr('text-anchor', 'middle')
      .attr('font-size', LABEL_FONT)
      .attr('stroke-width', 3)
      .text(function (d) { return d.tag; });

    restyleForZoom();
    scheduleLabels();
  }

  function touches(e, d) {
    return e.source.index === d.index || e.target.index === d.index;
  }

  function focused() {
    return locked || hovered;
  }

  function styleEdges() {
    var k = transform.k;
    var d = focused();
    if (!d) {
      edgeSel.attr('stroke', 'var(--edge)')
        .attr('stroke-width', 0.85 / k)
        .attr('stroke-opacity', Math.min(0.3, 0.17 + 0.05 / k));
      return;
    }
    edgeSel
      .attr('stroke', function (e) {
        if (e.target.index === d.index) return 'var(--in)';
        if (e.source.index === d.index) return 'var(--out)';
        return 'var(--edge)';
      })
      .attr('stroke-opacity', function (e) {
        return touches(e, d) ? 0.8 : 0.05;
      })
      .attr('stroke-width', function (e) {
        return (touches(e, d) ? 1.7 : 0.85) / k;
      });
  }

  function restyleForZoom() {
    styleEdges();
    nodeSel.selectAll('circle')
      .attr('stroke', function (d) {
        return (locked && locked.index === d.index) ? 'var(--in)' : '#fff';
      })
      .attr('stroke-width', function (d) {
        return ((locked && locked.index === d.index) ? 2.4 : 1.3) / transform.k;
      });
    if (locked) pinTip(locked);
  }

  var labelFrame = null;
  function scheduleLabels() {
    if (labelFrame) return;
    labelFrame = requestAnimationFrame(function () {
      labelFrame = null;
      placeLabels();
    });
  }

  function overlaps(box, boxes) {
    for (var i = 0; i < boxes.length; i += 1) {
      var o = boxes[i];
      if (box[0] < o[2] && box[2] > o[0] && box[1] < o[3] && box[3] > o[1]) {
        return true;
      }
    }
    return false;
  }

  /* Greedy declutter in screen space: hovered/searched papers get first pick,
     then the best connected ones; anything that would collide stays hidden. */
  function placeLabels() {
    var mode = document.getElementById('labels').value;
    var k = transform.k;
    var forced = {};
    var focus = focused();
    if (focus) {
      forced[focus.index] = true;
      neighbours[focus.index].inc.forEach(function (i) { forced[i] = true; });
      neighbours[focus.index].out.forEach(function (i) { forced[i] = true; });
    }
    if (matches) matches.forEach(function (i) { forced[i] = true; });

    // While focusing on one paper or a search hit, other labels are noise.
    var focusing = Boolean(focus) || Boolean(matches);
    var onlyForced = focusing || mode === 'none';

    var visible = {};
    if (!onlyForced || Object.keys(forced).length) {
      var cap = mode === 'all' || focusing
        ? nodes.length
        : Math.min(nodes.length, Math.round(80 * Math.pow(k, 1.15)));
      // Big circles are obstacles so an ordinary label never covers a hub;
      // labels of the focused paper's neighbours may overlap a circle.
      var obstacles = nodes.filter(function (d) { return d.r * k > 9; })
        .map(function (d) {
          var cx = transform.applyX(d.x);
          var cy = transform.applyY(d.y);
          var rr = d.r * k;
          return [cx - rr, cy - rr, cx + rr, cy + rr];
        });
      var boxes = [];
      var placed = 0;
      var ordered = nodes.slice().sort(function (a, b) {
        return (forced[b.index] ? 1e6 : 0) - (forced[a.index] ? 1e6 : 0)
          || b.score - a.score;
      });
      for (var i = 0; i < ordered.length && placed < cap; i += 1) {
        var d = ordered[i];
        if (onlyForced && !forced[d.index]) continue;
        var sx = transform.applyX(d.x);
        var cy = transform.applyY(d.y);
        if (sx < -60 || sx > plot.width + 60
            || cy < -40 || cy > plot.height + 40) {
          continue;
        }
        var half = d.tag.length * LABEL_FONT * 0.29 + 3;
        var below = cy + d.r * k + LABEL_FONT + 1.5;
        var above = cy - d.r * k - 3;
        var chosen = null;
        [below, above].forEach(function (sy) {
          if (chosen || sy < 8 || sy > plot.height - 4) return;
          var box = [sx - half, sy - LABEL_FONT, sx + half, sy + 3];
          var blocked = overlaps(box, boxes)
            || (!forced[d.index] && overlaps(box, obstacles));
          if (!blocked || d === focus) chosen = { sy: sy, box: box };
        });
        if (!chosen) continue;
        boxes.push(chosen.box);
        visible[d.index] = true;
        d.labelY = chosen.sy;
        placed += 1;
      }
    }
    if (focus) visible[focus.index] = true;
    labelSel
      .attr('display', function (d) {
        return visible[d.index] ? null : 'none';
      })
      .attr('x', function (d) { return transform.applyX(d.x); })
      .attr('y', function (d) { return d.labelY == null ? -50 : d.labelY; });
  }

  function related(d) {
    var set = {};
    set[d.index] = true;
    neighbours[d.index].inc.forEach(function (i) { set[i] = true; });
    neighbours[d.index].out.forEach(function (i) { set[i] = true; });
    return set;
  }

  function highlight(d) {
    var set = related(d);
    var hit = matches ? new Set(matches) : null;
    function isDim(n) {
      if (hit && !hit.has(n.index)) return true;
      return !set[n.index];
    }
    nodeSel.classed('dim', isDim)
      .classed('held', function (n) { return locked && n.index === locked.index; });
    labelSel.classed('dim', isDim);
    styleEdges();
    edgeSel.filter(function (e) { return touches(e, d); }).raise();
    nodeSel.filter(function (n) { return n.index === d.index; }).raise();
    scheduleLabels();
  }

  function clearHighlight() {
    nodeSel.classed('held', false);
    restyleForZoom();
    if (matches || tagFilter || citeFilterOn() || telegramFilterOn()) {
      applyFilters();
      return;
    }
    nodeSel.classed('dim', false);
    labelSel.classed('dim', false);
    scheduleLabels();
  }

  function enter(d, event) {
    if (locked) return;
    hovered = d;
    if (!matches || matches.indexOf(d.index) >= 0) highlight(d);
    showTip(d, event);
  }

  function leave() {
    if (locked) return;
    hovered = null;
    clearHighlight();
    tip.style('opacity', 0);
  }

  function lock(d, event) {
    locked = d;
    hovered = null;
    highlight(d);
    showTip(d, event);
    pinTip(d);
  }

  function unlock() {
    if (!locked) return;
    locked = null;
    hovered = null;
    clearHighlight();
    tip.style('opacity', 0);
  }

  function onClick(event, d) {
    event.preventDefault();
    event.stopPropagation();
    lock(d, event);
  }

  function onDblClick(event, d) {
    event.preventDefault();
    event.stopPropagation();
    window.open(d.url, '_blank');
  }

  function showTip(d, event) {
    var authors = (d.authors || []).slice(0, 3).join(', ')
      + ((d.authors || []).length > 3 ? ' et al.' : '');
    var when = d.date
      ? d.date + (d.date_source && d.date_source !== 'arxiv-api'
          ? ' (' + d.date_source.replace('-', ' ') + ')' : '')
      : 'date unknown';
    var hint = locked
      ? 'held \u00b7 double-click to open \u00b7 Esc to release'
      : 'click to hold \u00b7 double-click to open';
    tip.html('<b>' + escapeHtml(d.title) + '</b>'
      + '<div class="meta">' + (authors ? escapeHtml(authors) + ' &middot; ' : '')
      + when + '</div>'
      + '<div class="meta">' + escapeHtml(d.section) + ' &middot; ' + d.kind
      + (d.telegram ? ' &middot; telegram' : '')
      + (d.doc ? '' : ' &middot; no document retrieved') + '</div>'
      + (d.topic
        ? '<div class="meta">' + escapeHtml(d.topic)
          + ((d.ideas || []).length
            ? ' \u00b7 ' + d.ideas.map(escapeHtml).join(' \u00b7 ')
            : '')
          + '</div>'
        : '')
      + '<div class="counts">'
      + '<span class="in">cited by ' + d.cites + '</span>'
      + '<span class="out">cites ' + d.refs
      + (d.parentRefs !== d.refs ? ' (' + d.parentRefs + ' parents)' : '')
      + (d.childRefs !== d.refs ? ' (' + d.childRefs + ' nested)' : '')
      + (d.bonusAmount
        ? ' (+' + d.bonusAmount.toFixed(d.bonusAmount >= 10 ? 1 : 2) + ' bonus)'
        : '')
      + '</span>'
      + (d.lit_cites != null || d.lit_refs != null
        ? '<span class="meta">Litmaps ' + formatCount(d.lit_cites)
          + ' citations \u00b7 ' + formatCount(d.lit_refs) + ' refs</span>'
        : '')
      + (d.quality != null
        ? '<span class="meta">quality ' + formatQuality(d.quality)
          + (d.quality_models
            ? ' \u00b7 ' + (d.quality_accepts || 0) + '/' + d.quality_models
            : '')
          + (d.quality_verdict && d.quality_verdict !== 'KEEP'
            ? ' \u00b7 ' + d.quality_verdict
            : '')
          + '</span>'
        : '')
      + '<span class="meta">' + hint + '</span></div>');
    tip.style('opacity', 1);
    if (locked) pinTip(d);
    else moveTip(event);
  }

  function pinTip(d) {
    var box = tip.node().getBoundingClientRect();
    var sx = transform.applyX(d.x) + d.r * transform.k + 14;
    var sy = transform.applyY(d.y) - 12;
    if (sx + box.width > window.innerWidth - 8) {
      sx = transform.applyX(d.x) - d.r * transform.k - box.width - 14;
    }
    if (sy + box.height > window.innerHeight - 8) {
      sy = window.innerHeight - box.height - 8;
    }
    if (sy < 8) sy = 8;
    if (sx < 8) sx = 8;
    tip.style('left', sx + 'px').style('top', sy + 'px');
  }

  function moveTip(event) {
    var pad = 14;
    var box = tip.node().getBoundingClientRect();
    var x = event.clientX + pad;
    var y = event.clientY + pad;
    if (x + box.width > window.innerWidth - 8) x = event.clientX - box.width - pad;
    if (y + box.height > window.innerHeight - 8) {
      y = event.clientY - box.height - pad;
    }
    tip.style('left', x + 'px').style('top', y + 'px');
  }

  function escapeHtml(text) {
    return String(text == null ? '' : text).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function markLegend() {
    var el = document.getElementById('legend');
    if (!el) return;
    Array.prototype.forEach.call(el.querySelectorAll('span'), function (span) {
      var value = span.dataset.topic;
      var active = tagFilter == null
        ? value === ''
        : value === tagFilter;
      span.classList.toggle('on', active);
      span.classList.toggle('off', tagFilter != null && !active);
    });
  }

  function buildLegend() {
    var el = document.getElementById('legend');
    if (!el) return;
    var fieldCounts = {};
    var ideaCounts = {};
    var untagged = 0;
    nodes.forEach(function (d) {
      if (d.topic) fieldCounts[d.topic] = (fieldCounts[d.topic] || 0) + 1;
      else untagged += 1;
      (d.ideas || []).forEach(function (idea) {
        ideaCounts[idea] = (ideaCounts[idea] || 0) + 1;
      });
    });
    var seenFields = {};
    var families = [];
    (taxonomy.fields || []).forEach(function (field) {
      if (!fieldCounts[field.id]) return;
      seenFields[field.id] = true;
      var fam = field.family || 'Other';
      var group = families.find(function (g) { return g.name === fam; });
      if (!group) {
        group = {name: fam, ids: []};
        families.push(group);
      }
      group.ids.push(field.id);
    });
    var extraFields = Object.keys(fieldCounts).filter(function (id) {
      return !seenFields[id];
    }).sort();
    var ideas = (taxonomy.ideas || []).filter(function (idea) {
      return ideaCounts[idea];
    });
    el.innerHTML = '';
    function row(title) {
      var wrap = document.createElement('div');
      wrap.className = 'legend-row';
      if (title) {
        var label = document.createElement('b');
        label.className = 'legend-label';
        label.textContent = title;
        wrap.appendChild(label);
      }
      el.appendChild(wrap);
      return wrap;
    }
    function chip(parent, label, color, value, isIdea) {
      var span = document.createElement('span');
      span.dataset.topic = value == null ? '' : value;
      var swatch = document.createElement('i');
      swatch.className = isIdea ? 'swatch idea' : 'swatch';
      if (isIdea) swatch.style.borderColor = color || IDEA_STROKE;
      else swatch.style.background = color;
      span.appendChild(swatch);
      span.appendChild(document.createTextNode(label));
      span.addEventListener('click', function () {
        tagFilter = tagFilter === value ? null : value;
        applyFilters();
        markLegend();
        savePrefs();
      });
      parent.appendChild(span);
    }
    function famLabel(parent, name) {
      var b = document.createElement('b');
      b.className = 'fam';
      b.textContent = name;
      parent.appendChild(b);
    }
    var fieldRow = row('fields');
    chip(fieldRow, 'all', '#8b959c', null, false);
    if (untagged) chip(fieldRow, 'untagged ' + untagged, UNTAGGED, 'untagged', false);
    families.forEach(function (group) {
      famLabel(fieldRow, group.name);
      group.ids.forEach(function (field) {
        chip(fieldRow, field + ' ' + fieldCounts[field],
             TOPIC_COLOR[field] || UNTAGGED, field, false);
      });
    });
    if (extraFields.length) {
      famLabel(fieldRow, 'extra');
      extraFields.forEach(function (field) {
        chip(fieldRow, field + ' ' + fieldCounts[field],
             TOPIC_COLOR[field] || UNTAGGED, field, false);
      });
    }
    if (ideas.length) {
      var ideaRow = row('ideas');
      ideas.forEach(function (idea) {
        chip(ideaRow, idea + ' ' + ideaCounts[idea],
             IDEA_STROKE, idea, true);
      });
    }
    markLegend();
  }

  function runSearch() {
    applyFilters();
  }

  function citeFilterOn() {
    var el = document.getElementById('citefilter');
    return Boolean(el && el.checked);
  }

  function telegramFilterOn() {
    var el = document.getElementById('tgfilter');
    return Boolean(el && el.checked);
  }

  function applyFilters() {
    var term = document.getElementById('search').value.trim().toLowerCase();
    var citeOn = citeFilterOn();
    var tgOn = telegramFilterOn();
    var filtering = Boolean(term) || Boolean(tagFilter) || citeOn || tgOn;
    matches = null;
    if (filtering) {
      matches = nodes.filter(function (d) {
        if (citeOn && !citesSeed[d.index]) return false;
        if (tgOn && !d.telegram) return false;
        if (term && d.haystack.indexOf(term) < 0) return false;
        if (tagFilter === 'untagged') return !d.topic;
        if (tagFilter && FIELD_SET[tagFilter]) return d.topic === tagFilter;
        if (tagFilter) {
          return (d.ideas || []).indexOf(tagFilter) >= 0
            || (d.tags || []).indexOf(tagFilter) >= 0;
        }
        return true;
      }).map(function (d) { return d.index; });
    }
    var hit = matches ? new Set(matches) : null;
    nodeSel.classed('dim', function (d) { return hit ? !hit.has(d.index) : false; });
    labelSel.classed('dim', function (d) { return hit ? !hit.has(d.index) : false; });
    nodeSel.selectAll('circle')
      .attr('stroke', function (d) {
        return hit && hit.has(d.index) ? 'var(--in)' : '#fff';
      })
      .attr('stroke-width', function (d) {
        return (hit && hit.has(d.index) ? 2.4 : 1.3) / transform.k;
      });
    document.getElementById('note').textContent = note(hit ? hit.size : null);
    if (locked) highlight(locked);
    else scheduleLabels();
  }

  function sizeNote() {
    var mode = yMode();
    if (mode === 'cited' || mode === 'citations') return '';
    return '  \u00b7  size: cited by on this list';
  }

  function note(hitCount) {
    var base = 'x: publication date  \u00b7  ' + yNote()
      + sizeNote()
      + (qualityColorOn() ? '  \u00b7  colour: aggregated quality' : '')
      + '  \u00b7  edges parsed from arXiv/ar5iv HTML, page HTML and'
      + ' Crossref  \u00b7  built ' + data.generated;
    return hitCount == null ? base : hitCount + ' matching entries  \u00b7  ' + base;
  }

  function stats() {
    var withDoc = nodes.filter(function (d) { return d.doc; }).length;
    var linked = nodes.filter(function (d) { return d.cites || d.refs; }).length;
    var undated = nodes.filter(function (d) { return !d.time; }).length;
    return nodes.length + ' entries \u00b7 ' + edges.length + ' citation links \u00b7 '
      + withDoc + ' documents read \u00b7 ' + linked + ' connected \u00b7 '
      + undated + ' undated';
  }

  function redraw() {
    layout();
    redrawAxes();
    render();
    if (matches || tagFilter || citeFilterOn() || telegramFilterOn()) {
      applyFilters();
    }
  }

  document.getElementById('labels').addEventListener('change', function () {
    savePrefs();
    scheduleLabels();
  });
  function applyYAxis() {
    syncAddCited();
    document.getElementById('note').textContent = note(
      matches ? matches.length : null);
    svg.call(zoom.transform, d3.zoomIdentity);
    redraw();
  }
  document.getElementById('yaxis').addEventListener('change', function () {
    savePrefs();
    applyYAxis();
  });
  document.getElementById('addcited').addEventListener('change', function () {
    savePrefs();
    applyYAxis();
  });
  document.getElementById('edges').addEventListener('change', function () {
    savePrefs();
    syncEdges();
  });
  document.getElementById('search').addEventListener('input', runSearch);
  document.getElementById('citefilter').addEventListener('change', function () {
    savePrefs();
    runSearch();
  });
  document.getElementById('tgfilter').addEventListener('change', function () {
    savePrefs();
    runSearch();
  });
  document.getElementById('qcolor').addEventListener('change', function () {
    savePrefs();
    restyleFills();
    document.getElementById('note').textContent = note(
      matches ? matches.length : null);
  });

  function restyleFills() {
    if (!nodeSel) return;
    nodeSel.selectAll('circle')
      .attr('fill', nodeFill)
      .attr('fill-opacity', nodeFillOpacity);
  }
  document.getElementById('reset').addEventListener('click', function () {
    unlock();
    svg.transition().duration(350).call(zoom.transform, d3.zoomIdentity);
  });
  svg.on('click', function (event) {
    if (event.target.tagName !== 'circle') unlock();
  });
  window.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (locked) {
      unlock();
      return;
    }
    document.getElementById('search').value = '';
    document.getElementById('citefilter').checked = false;
    document.getElementById('tgfilter').checked = false;
    tagFilter = null;
    markLegend();
    savePrefs();
    runSearch();
  });

  var resizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(redraw, 180);
  });

  buildLegend();
  syncAddCited();
  document.getElementById('stats').textContent = stats();
  document.getElementById('note').textContent = note(null);
  redraw();
  syncEdges();
  if (matches || tagFilter || citeFilterOn() || telegramFilterOn()) {
    applyFilters();
  }
}());
