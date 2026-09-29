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
   nodes apart inside a per-node box. Crowded rows (same y, neighbours
   a few pixels away) get a wider box; leftovers are separated after
   the last tick, then shrunk if the box cannot fit. Scored / counted
   disks stay above the zero / n/a rule (edge, not just center).
   Selection is mirrored into #sel=<key>,… and restored on load.
   A selected paper wears a dashed ring one pixel outside the disk.
   The pinned tooltip sits where it covers the
   fewest selected papers and links. Each hold (a click or a deep
   link) plays an animated double-click hint, once the tab is visible. */
(function () {
  'use strict';

  var data = window.GRAPH_DATA;
  var MARGIN = { top: 74, right: 96, bottom: 62, left: 62 };
  var TOP_PAD = 72;          // between plot.top and the highest row
  var GUTTER = 132;          // parking band for entries with no known date
  var ZERO_BAND = 78;        // breathing room for zeros / missing y-values
  // Phone (html.compact): the header is one 34px button in the corner, the
  // footer is a single line, and the plot keeps nearly the whole height.
  var MARGIN_COMPACT = { top: 20, right: 44, bottom: 34, left: 44 };
  var TOP_PAD_COMPACT = 24;
  var ZERO_BAND_COMPACT = 44;
  var LABEL_FONT = 10.5;
  var NODE_STROKE = 1.3;    // screen px; white disk outline, same tone as the page
  var HIT_STROKE = 2.4;     // screen px; orange outline on a search or filter hit
  var RING_OUTSET = 1;      // screen px of page between the disk and the dashes
  var RING_WIDTH = 2;
  var RING_PERIOD = 9;       // screen px per dash + gap
  var RING_DASHES = [4, 8];
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
  var headerEl = document.querySelector('header');

  /* d3.pointer and every d3-zoom gesture invert svg.getScreenCTM(). WebKit
     before spring 2026 (bugs 209220 / 308970) dropped the body's CSS
     rotation from that matrix, so on such an iPhone the html.rotated page
     would pan sideways. Probe once the turn is in effect; if the matrix
     lacks it, answer with the known one: body (x, y) -> client
     (bodyHeight - y, x), i.e. a=0 b=1 c=-1 d=0 e=bodyHeight f=0. */
  var ctmShimmed = false;
  function shimScreenCtm(rotated) {
    if (!rotated || ctmShimmed) return;
    var node = svg.node();
    var m = node.getScreenCTM();
    if (!m || Math.abs(m.b) > 0.5) return;
    var native = node.getScreenCTM;
    node.getScreenCTM = function () {
      if (!document.documentElement.classList.contains('rotated')) {
        return native.call(this);
      }
      var r = this.createSVGMatrix();
      r.a = 0; r.b = 1; r.c = -1; r.d = 0;
      r.e = document.body.clientHeight; r.f = 0;
      return r;
    };
    ctmShimmed = true;
  }

  var gAxes = svg.append('g');
  var gRoot = svg.append('g');
  var gEdges = gRoot.append('g').attr('class', 'edges');
  var gNodes = gRoot.append('g').attr('class', 'nodes');
  // The ring is outside the zoom transform, so its 1px gap stays 1px.
  var gRings = svg.append('g').attr('class', 'rings');
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

  function plotScale() {
    if (!plot || !plot.width || !plot.height) return 1;
    var area = (plot.width / 1440) * (plot.height / 860);
    // A phone is a quarter of the reference area; the square root keeps the
    // disks at a tappable 2 to 11px instead of 1 to 5px.
    return Math.min(1, plot.compact ? Math.sqrt(area) : area);
  }

  function applyMetric() {
    var s = plotScale();
    radius = d3.scaleSqrt()
      .domain([0, d3.max(nodes, sizeValue) || 1])
      .range([4 * s, 21 * s]);
    if (qualityMode()) {
      maxY = 1;
      nodes.forEach(function (d) {
        var q = d.quality;
        d.r = radius(sizeValue(d));
        if (!hasY(d)) d.r = Math.min(d.r, 6 * s);
        d.score = (q == null ? 0 : q + 1) * 2 + (d.cites + d.refs) * 0.5;
      });
      return;
    }
    maxY = d3.max(nodes, yCount) || 1;
    nodes.forEach(function (d) {
      var yv = yCount(d);
      d.r = radius(sizeValue(d));
      if (!hasY(d)) d.r = Math.min(d.r, 6 * s);
      d.score = yv * 2 + (d.cites + d.refs - yv) * 0.5;
    });
  }
  applyMetric();

  var xBase, yBase, transform = d3.zoomIdentity, plot = {};
  var hovered = null, locked = null, matches = null, hitSet = null, tagFilter = null;
  var filterKey = '';
  var selected = [];   // ordered node indices; the last one is the held paper (locked)
  var byId = Object.create(null);
  nodes.forEach(function (d) { byId[d.id] = d.index; });
  var HASH_KEY = 'sel';
  var TIP_CELL = 10;
  var TIP_GAP = 14;
  var TIP_HIT = 1000;     // one cell of a selected disk or its label
  var TIP_LINK = 4;       // one cell of a highlighted link or neighbour disk
  var TIP_DIST = 0.05;    // per px beyond the held disk, so the tip stays near it
  var TIP_STICKY = 8;     // keep the current spot unless a new one is this much cheaper
  var tipSize = null;
  var tipOffset = null;
  var PREFS_KEY = 'key-papers-map-prefs';
  var GHOST_DELAY = 3000;
  var GHOST_GLIDE = 700;
  var GHOST_BOW = 16;
  var GHOST_PAUSE = 200;     // a hidden tab's next frame jumps by seconds
  var GHOST_STEPS = [
    { at: 820, kind: 'press' },
    { at: 910, kind: 'release' },
    { at: 1020, kind: 'press' },
    { at: 1110, kind: 'release' },
    { at: 1500, kind: 'fade' },
    { at: 1700, kind: 'done' }
  ];
  var ghost = d3.select('#ghost');
  var ghostRun = null;
  var ghostTimer = null;
  var ghostHold = null;     // queued while the tab is hidden

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
    // Body sizes are layout sizes: on a phone held upright (html.rotated)
    // the body is drawn turned 90 degrees, and these stay in its own pixels.
    var width = document.body.clientWidth;
    var height = document.body.clientHeight;
    var compact = document.documentElement.classList.contains('compact');
    shimScreenCtm(document.documentElement.classList.contains('rotated'));
    var m = compact ? MARGIN_COMPACT : MARGIN;
    var topPad = compact ? TOP_PAD_COMPACT : TOP_PAD;
    var zeroBand = compact ? ZERO_BAND_COMPACT : ZERO_BAND;
    // On a phone the header is a corner button or an overlay drawer, so it
    // takes no band of its own.
    var headerH = compact ? 0 : headerEl.offsetHeight;
    plot = {
      compact: compact,
      left: m.left,
      right: width - m.right,
      top: compact ? m.top : Math.max(m.top, headerH + 22),
      bottom: height - m.bottom,
      width: width,
      height: height,
      headerBottom: headerH
    };
    plot.gutter = nodes.some(function (d) { return !d.time; }) ? GUTTER : 0;
    var timeLeft = plot.left + plot.gutter + (plot.gutter ? 30 : 0);
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
          .range([plot.bottom - zeroBand, plot.top + topPad])
      : d3.scaleLinear()
          .domain([yEncode(1), 1])
          .range([plot.bottom - zeroBand, plot.top + topPad]);

    // Uncited / unscored entries would otherwise pile onto a single pixel row.
    plot.zeroLow = plot.bottom - 12;
    plot.zeroHigh = plot.bottom - zeroBand + 16;
    plot.zeroRule = plot.bottom - zeroBand + 6;

    var gutterMid = plot.left + plot.gutter / 2;
    var s = plotScale();
    var timeW = plot.right - timeLeft;
    var monthMs = 30 * 24 * 3600 * 1000;
    var dxMonth = Math.abs(
      xBase(new Date(+span[0] + monthMs)) - xBase(new Date(+span[0]))
    );
    if (!isFinite(dxMonth)) dxMonth = 12 * s;
    var dxMax = Math.min(24 * s, Math.max(12 * s, dxMonth, 0.022 * timeW));
    var dxZero = Math.min(48 * s, Math.max(dxMax, 0.04 * timeW));
    function yRow(v) {
      if (v <= 0) return plot.zeroRule;
      return yBase(yEncode(v));
    }
    var PACK_GAP = 0.65;
    var OVERLAP_EPS = 0.5;
    var occ = {};
    var occKeys = [];
    if (!qualityMode()) {
      nodes.forEach(function (d) {
        if (!hasY(d)) return;
        var v = yCount(d);
        occ[v] = (occ[v] || 0) + 1;
      });
      occKeys = Object.keys(occ).map(Number).sort(function (a, b) {
        return a - b;
      });
    }
    function occIndex(yv) {
      var best = 0;
      var bestD = Infinity;
      for (var i = 0; i < occKeys.length; i++) {
        var dlt = Math.abs(occKeys[i] - yv);
        if (dlt < bestD) {
          bestD = dlt;
          best = i;
        }
      }
      return best;
    }
    function nearestOccGap(yv, fromY) {
      var idx = occIndex(yv);
      var best = Infinity;
      if (idx > 0) {
        best = Math.min(best, Math.abs(fromY - yRow(occKeys[idx - 1])));
      }
      if (idx + 1 < occKeys.length) {
        best = Math.min(best, Math.abs(fromY - yRow(occKeys[idx + 1])));
      }
      return best;
    }
    // Walk occupied y-values, not yv±1, so fractional bonusRefs
    // neighbours are the next papers, not empty integer ticks.
    function visualGap(fromY, yv, dir, minPx) {
      if (minPx == null) minPx = 40 * s;
      if (dir < 0 && yv <= 1) return Math.max(0, plot.zeroRule - fromY);
      if (!occKeys.length) return 0;
      var idx = occIndex(yv);
      var step = 1;
      var gap = 0;
      while (step <= occKeys.length && gap < minPx) {
        var ni = idx + dir * step;
        if (ni < 0) return Math.max(0, plot.zeroRule - fromY);
        if (ni >= occKeys.length) return Math.max(0, fromY - plot.top);
        gap = dir * (fromY - yRow(occKeys[ni]));
        step += 1;
      }
      return Math.max(0, gap);
    }
    function clampNode(d) {
      d.x = Math.max(d.xLo, Math.min(d.xHi, d.x));
      d.y = Math.max(Math.max(plot.top, d.yLo),
                     Math.min(Math.min(plot.bottom, d.yHi), d.y));
    }
    // Keep the disk, not just the center, out of the 0 / n/a gutter.
    function fitAboveZero(d) {
      if (!hasY(d)) {
        d.zeroEdge = null;
        return;
      }
      d.zeroEdge = plot.zeroRule;
      d.yHi = d.yHiBand;
      var room = plot.zeroRule - d.yLo;
      if (room > 2 * s) d.r = Math.min(d.r, room - 0.5);
      d.yHi = Math.min(d.yHiBand, plot.zeroRule - d.r);
      if (d.yHi < d.yLo) d.yHi = d.yLo;
    }
    nodes.forEach(function (d, i) {
      var wobble = ((i * 2654435761) % 1000) / 1000 - 0.5;
      d.tx = d.time ? xBase(d.time) : gutterMid + wobble * (plot.gutter - 26);
      d.ty = hasY(d)
        ? (qualityMode() ? yBase(d.quality) : yBase(yEncode(yCount(d))))
          + wobble * 4
        : plot.zeroLow - (wobble + 0.5) * (plot.zeroLow - plot.zeroHigh);
      d.x = d.tx;
      d.y = d.ty;
      d.vx = 0;
      d.vy = 0;
      d.undated = !d.time;
      var yv = hasY(d) && !qualityMode() ? yCount(d) : 0;
      var occN = occ[yv] || 1;
      var tight = Boolean(yv) && occN >= 6 && nearestOccGap(yv, d.ty) < 16 * s;
      if (d.undated) {
        d.xLo = plot.left + d.r;
        d.xHi = plot.left + plot.gutter - d.r;
      } else {
        var dx = hasY(d) ? dxMax : dxZero;
        if (tight) {
          dx = Math.min(dxMax * 1.85, dx * (1 + 0.1 * Math.sqrt(occN)));
        }
        d.xLo = Math.max(timeLeft - 14, d.tx - dx);
        d.xHi = Math.min(plot.right + 26, d.tx + dx);
      }
      if (!hasY(d)) {
        d.yLo = plot.zeroHigh;
        d.yHi = plot.zeroLow;
      } else if (qualityMode()) {
        // zeroRule, not plot.bottom: scored dots must not enter the n/a band.
        var qPad = 16 * s;
        d.yLo = Math.max(plot.top, d.ty - qPad);
        d.yHi = Math.min(plot.zeroRule, d.ty + qPad);
      } else {
        var minPx = tight ? Math.max(40 * s, 18 * s * Math.sqrt(occN)) : 40 * s;
        var cap = tight
          ? Math.min(42 * s, Math.max(24 * s, 11 * s * Math.sqrt(occN)))
          : 24 * s;
        var frac = tight ? 0.78 : 0.5;
        var up = Math.min(frac * visualGap(d.ty, yv, 1, minPx), cap);
        var down = yv <= 1
          ? Math.max(0, Math.min(plot.zeroRule - d.ty, 6 * s))
          : Math.min(frac * visualGap(d.ty, yv, -1, minPx), cap);
        d.yLo = Math.max(plot.top, d.ty - up);
        d.yHi = Math.min(plot.zeroRule, d.ty + down);
      }
      d.yHiBand = d.yHi;
      var box = Math.min(d.xHi - d.xLo, d.yHi - d.yLo);
      if (box > 0) {
        d.r = Math.min(d.r, Math.max(2 * s, Math.min(0.3 * box, box / 2)));
      }
      fitAboveZero(d);
    });

    var sim = d3.forceSimulation(nodes)
      .force('x', d3.forceX(function (d) { return d.tx; }).strength(0.25))
      .force('y', d3.forceY(function (d) { return d.ty; }).strength(0.22))
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
    nodes.forEach(clampNode);

    function separatePairs(maxPass) {
      var leftover = 0;
      for (var pass = 0; pass < maxPass; pass++) {
        leftover = 0;
        for (var i = 0; i < nodes.length; i++) {
          var a = nodes[i];
          for (var j = i + 1; j < nodes.length; j++) {
            var b = nodes[j];
            var dx = b.x - a.x;
            var dy = b.y - a.y;
            var dist = Math.hypot(dx, dy);
            var need = a.r + b.r + PACK_GAP;
            if (dist >= need) continue;
            leftover += 1;
            if (dist < 0.05) {
              var ang = ((i * 57 + j * 13) % 360) * Math.PI / 180;
              dx = Math.cos(ang);
              dy = Math.sin(ang);
              dist = 1;
            }
            var push = (need - dist) / 2;
            var ux = dx / dist;
            var uy = dy / dist;
            a.x -= ux * push;
            a.y -= uy * push;
            b.x += ux * push;
            b.y += uy * push;
            clampNode(a);
            clampNode(b);
          }
        }
        if (!leftover) return 0;
      }
      return leftover;
    }
    separatePairs(40);
    for (var shrink = 0; shrink < 12; shrink++) {
      var hit = {};
      var stubborn = 0;
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j];
          if (Math.hypot(b.x - a.x, b.y - a.y) < a.r + b.r - OVERLAP_EPS) {
            hit[i] = true;
            hit[j] = true;
            stubborn += 1;
          }
        }
      }
      if (!stubborn) break;
      Object.keys(hit).forEach(function (k) {
        var n = nodes[+k];
        n.r = Math.max(2 * s, n.r * 0.88);
        fitAboveZero(n);
      });
      separatePairs(16);
    }
    nodes.forEach(function (d) {
      fitAboveZero(d);
      clampNode(d);
    });
    plot.timeLeft = timeLeft;
  }

  function edgeControl(e) {
    var a = e.source, b = e.target;
    var dx = b.x - a.x, dy = b.y - a.y;
    var len = Math.hypot(dx, dy) || 1;
    var bow = Math.min(70, len * 0.15);
    return {
      x: (a.x + b.x) / 2 - (dy / len) * bow,
      y: (a.y + b.y) / 2 + (dx / len) * bow
    };
  }

  function edgePath(e) {
    var a = e.source, b = e.target, c = edgeControl(e);
    return 'M' + a.x + ',' + a.y + 'Q' + c.x + ',' + c.y + ' ' + b.x + ',' + b.y;
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

    // On a phone the bottom band only holds the tick labels and the footer;
    // the years speak for themselves.
    if (!plot.compact) {
      gAxes.append('text')
        .attr('class', 'caption')
        .attr('text-anchor', 'middle')
        .attr('x', (plot.timeLeft + plot.right) / 2)
        .attr('y', plot.bottom + 42)
        .text('more recently published \u2192');
    }

    gAxes.append('text')
      .attr('class', 'caption')
      .attr('transform', 'translate(' + (plot.right + (plot.compact ? 28 : 44))
        + ',' + (plot.top + plot.bottom) / 2 + ') rotate(-90)')
      .attr('text-anchor', 'middle')
      .text(yAxisCaption());

    if (plot.gutter) {
      var gutterEnd = transform.applyX(plot.left + plot.gutter + 12);
      gAxes.append('line')
        .attr('class', 'gutter-rule')
        .attr('x1', gutterEnd).attr('x2', gutterEnd)
        .attr('y1', plot.top - 12).attr('y2', plot.bottom);
    }
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

  function styleEdges() {
    var k = transform.k;
    var focus = focusIndices();
    if (!focus.length) {
      edgeSel.attr('stroke', 'var(--edge)')
        .attr('stroke-width', 0.85 / k)
        .attr('stroke-opacity', Math.min(0.3, 0.17 + 0.05 / k));
      return;
    }
    var inFocus = {};
    focus.forEach(function (i) { inFocus[i] = true; });
    edgeSel
      .attr('stroke', function (e) {
        if (locked && inFocus[e.source.index] && inFocus[e.target.index]) {
          if (e.target.index === locked.index) return 'var(--in)';
          if (e.source.index === locked.index) return 'var(--out)';
        }
        if (inFocus[e.target.index]) return 'var(--in)';
        if (inFocus[e.source.index]) return 'var(--out)';
        return 'var(--edge)';
      })
      .attr('stroke-opacity', function (e) {
        return (inFocus[e.source.index] || inFocus[e.target.index]) ? 0.8 : 0.05;
      })
      .attr('stroke-width', function (e) {
        return ((inFocus[e.source.index] || inFocus[e.target.index]) ? 1.7 : 0.85) / k;
      });
  }

  function isHit(index) {
    return Boolean(hitSet && hitSet.has(index));
  }

  // Screen px from the disk radius to the ring's outer edge. The white
  // outline matches the page, so its gap is measured from the fill. An
  // orange hit outline is visible, so the gap starts outside that stroke.
  function ringPast(orange) {
    var stroke = orange ? HIT_STROKE : NODE_STROKE;
    var edge = orange ? stroke / 2 : -stroke / 2;
    return edge + RING_OUTSET + RING_WIDTH;
  }

  function styleNodeStrokes() {
    nodeSel.selectAll('circle')
      .attr('stroke', function (d) {
        return isHit(d.index) ? 'var(--in)' : '#fff';
      })
      .attr('stroke-width', function (d) {
        return (isHit(d.index) ? HIT_STROKE : NODE_STROKE) / transform.k;
      });
  }

  function ringDash(rScreen) {
    var c = 2 * Math.PI * rScreen;
    var n = Math.max(RING_DASHES[0],
                     Math.min(RING_DASHES[1], Math.floor(c / RING_PERIOD)));
    var period = 100 / n;
    var cap = RING_WIDTH * 100 / c;   // round caps eat this from each gap
    var gap = Math.min(period * 0.8, period * 0.45 + cap);
    return (period - gap) + ' ' + gap;
  }

  function drawRings() {
    var k = transform.k;
    var ringR = function (d) {
      return d.r * k + ringPast(isHit(d.index)) - RING_WIDTH / 2;
    };
    var sel = gRings.selectAll('g.sel')
      .data(selected.map(function (i) { return nodes[i]; }), function (d) {
        return d.id;
      })
      .join(function (enter) {
        var g = enter.append('g').attr('class', 'sel');
        g.append('circle').attr('class', 'sel-ring').attr('pathLength', 100);
        return g;
      });
    var nodeEls = nodeSel.nodes();
    sel
      .classed('dim', function (d) {
        return nodeEls[d.index].classList.contains('dim');
      })
      .attr('transform', function (d) {
        return 'translate(' + transform.applyX(d.x) + ','
          + transform.applyY(d.y) + ')';
      });
    sel.select('.sel-ring')
      .attr('r', ringR)
      .attr('stroke-width', RING_WIDTH)
      .attr('stroke-dasharray', function (d) { return ringDash(ringR(d)); });
  }

  function restyleForZoom() {
    styleEdges();
    styleNodeStrokes();
    drawRings();
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

  function labelBox(d, sx, sy) {
    var half = d.tag.length * LABEL_FONT * 0.29 + 3;
    return [sx - half, sy - LABEL_FONT, sx + half, sy + 3];
  }

  function labelGap(d) {
    return isSelected(d.index) ? ringPast(isHit(d.index)) + 1 : 0;
  }

  function labelSlots(cy, rr, gap) {
    return [cy + rr + gap + LABEL_FONT + 1.5, cy - rr - gap - 3];
  }

  // Selected labels ignore collisions and take the first spot that fits
  // vertically, which is what placeLabels does for the focused papers.
  function selectedLabelBox(d) {
    var sx = transform.applyX(d.x);
    var cy = transform.applyY(d.y);
    var rr = d.r * transform.k;
    var slots = labelSlots(cy, rr, labelGap(d));
    var below = slots[0];
    var above = slots[1];
    if (below >= 8 && below <= plot.height - 4) return labelBox(d, sx, below);
    if (above >= 8 && above <= plot.height - 4) return labelBox(d, sx, above);
    return null;
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
    var focus = focusIndices();
    var inFocus = {};
    focus.forEach(function (i) {
      inFocus[i] = true;
      Object.assign(forced, related(nodes[i]));
    });
    if (matches) matches.forEach(function (i) { forced[i] = true; });

    // While focusing on one paper or a search hit, other labels are noise.
    var focusing = focus.length > 0 || Boolean(matches);
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
        var slots = labelSlots(cy, d.r * k, labelGap(d));
        var below = slots[0];
        var above = slots[1];
        var chosen = null;
        [below, above].forEach(function (sy) {
          if (chosen || sy < 8 || sy > plot.height - 4) return;
          var box = labelBox(d, sx, sy);
          var blocked = overlaps(box, boxes)
            || (!forced[d.index] && overlaps(box, obstacles));
          if (!blocked || inFocus[d.index]) chosen = { sy: sy, box: box };
        });
        if (!chosen) continue;
        boxes.push(chosen.box);
        visible[d.index] = true;
        d.labelY = chosen.sy;
        placed += 1;
      }
    }
    focus.forEach(function (i) { visible[i] = true; });
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

  function isSelected(i) { return selected.indexOf(i) >= 0; }

  function sameList(a, b) {
    if (a.length !== b.length) return false;
    for (var i = 0; i < a.length; i += 1) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  }

  function focusIndices() {
    if (selected.length) return selected;
    return hovered ? [hovered.index] : [];
  }

  function setSelection(indices) {
    selected = indices.slice();
    locked = selected.length ? nodes[selected[selected.length - 1]] : null;
    if (!ghostRun || ghostRun.d !== locked) cancelGhost();
    hovered = null;
    if (locked) {
      highlight();
      showTip(locked, null);
    } else {
      clearHighlight();
      tip.style('opacity', 0);
    }
    syncHash();
    syncShareButton();
  }

  function toggleSelected(d) {
    var next = selected.filter(function (i) { return i !== d.index; });
    if (next.length === selected.length) next.push(d.index);
    setSelection(next);
  }

  function encodeKey(id) {
    // : / ~ stay literal. ? is escaped so a chat/proxy that splits on the
    // first ? does not steal the rest of a url: key as a query string.
    return encodeURI(id).replace(/[,&#?]/g, function (c) {
      return encodeURIComponent(c);
    });
  }

  function selectionHash() {
    if (!selected.length) return '';
    return '#' + HASH_KEY + '=' + selected.map(function (i) {
      return encodeKey(nodes[i].id);
    }).join(',');
  }

  function shareUrl() {
    return window.location.href.split('#')[0] + selectionHash();
  }

  function syncHash() {
    var url = window.location.pathname + window.location.search + selectionHash();
    window.history.replaceState(null, '', url);
  }

  function parseHash(hash) {
    var raw = String(hash || '').replace(/^#/, '');
    var value = null;
    raw.split('&').forEach(function (part) {
      var eq = part.indexOf('=');
      if (eq > 0 && part.slice(0, eq) === HASH_KEY) value = part.slice(eq + 1);
    });
    if (!value) return [];
    var out = [];
    value.split(',').forEach(function (piece) {
      var id;
      try { id = decodeURIComponent(piece); } catch (err) { return; }
      if (/^\d{4}\.\d{4,5}$/.test(id)) id = 'arxiv:' + id;
      var idx = byId[id];
      if (typeof idx === 'number' && idx === (idx | 0)
          && idx >= 0 && idx < nodes.length && out.indexOf(idx) < 0) {
        out.push(idx);
      }
    });
    return out;
  }

  function applyHash(fromHashChange) {
    var indices = parseHash(window.location.hash);
    var same = sameList(indices, selected);
    if (!same) {
      setSelection(indices);
    } else if (window.location.hash !== selectionHash()) {
      syncHash();
    }
    if (fromHashChange && locked) queueGhost(locked);
  }

  window.addEventListener('hashchange', function () { applyHash(true); });

  function syncShareButton() {
    var button = document.getElementById('share');
    button.disabled = !selected.length;
    if (!selected.length) button.textContent = 'copy link';
  }

  document.getElementById('share').addEventListener('click', function () {
    if (!selected.length) return;
    var button = this;
    function done(ok) {
      button.textContent = ok ? 'copied' : 'copy failed';
      setTimeout(function () { button.textContent = 'copy link'; }, 1400);
    }
    var url = shareUrl();
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { done(true); },
                                             function () { done(false); });
    } else {
      window.prompt('Copy this link', url);
      done(true);
    }
  });

  function highlight() {
    var focus = focusIndices();
    var set = {};
    focus.forEach(function (i) { Object.assign(set, related(nodes[i])); });
    function isDim(n) {
      if (hitSet && !isHit(n.index)) return true;
      return !set[n.index];
    }
    nodeSel.classed('dim', isDim)
      .classed('held', function (n) { return isSelected(n.index); });
    labelSel.classed('dim', isDim);
    styleEdges();
    edgeSel.filter(function (e) {
      return focus.some(function (i) { return touches(e, nodes[i]); });
    }).raise();
    focus.forEach(function (i) {
      nodeSel.filter(function (n) { return n.index === i; }).raise();
    });
    drawRings();
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
    if (!matches || matches.indexOf(d.index) >= 0) highlight();
    showTip(d, event);
  }

  function leave() {
    if (locked) return;
    hovered = null;
    clearHighlight();
    tip.style('opacity', 0);
  }

  function unlock() {
    if (!selected.length) return;
    setSelection([]);
  }

  function cancelGhost() {
    if (ghostTimer) {
      clearTimeout(ghostTimer);
      ghostTimer = null;
    }
    ghostHold = null;
    if (ghostRun && ghostRun.frame) cancelAnimationFrame(ghostRun.frame);
    ghost.classed('on', false).classed('press', false);
    ghost.selectAll('.ring').remove();
    ghostRun = null;
  }

  function ghostFrame(now) {
    var run = ghostRun;
    if (!run) return;
    if (document.hidden) {
      run.frame = 0;
      return;
    }
    var d = run.d;
    var elapsed = now - run.t0;
    if (elapsed < 0) elapsed = 0;
    // rAF does not run in a background tab, so the next timestamp skips
    // the whole hint. Treat that gap as a pause and keep the timeline.
    if (run.lastAt) {
      var gap = now - run.lastAt;
      if (gap > GHOST_PAUSE) {
        run.t0 += gap;
        elapsed = Math.max(0, now - run.t0);
      }
    } else if (elapsed > GHOST_PAUSE) {
      run.t0 = now;
      elapsed = 0;
    }
    run.lastAt = now;
    var glide = run.calm ? 1 : Math.min(1, elapsed / GHOST_GLIDE);
    var u = glide >= 1 ? 1 : d3.easeCubicInOut(glide);
    var hx = transform.applyX(d.x);
    var hy = transform.applyY(d.y);
    var bow = Math.sin(Math.PI * glide) * GHOST_BOW;
    var x = run.sx + (hx - run.sx) * u + run.nx * bow;
    var y = run.sy + (hy - run.sy) * u + run.ny * bow;
    ghost.style('transform', 'translate(' + x + 'px,' + y + 'px)');
    while (run.step < GHOST_STEPS.length && elapsed >= GHOST_STEPS[run.step].at) {
      var kind = GHOST_STEPS[run.step].kind;
      run.step += 1;
      if (kind === 'press') {
        ghost.classed('press', true);
        var rr = d.r * transform.k;
        var size = Math.max(36, rr * 2 + 20);
        ghost.append('span').attr('class', 'ring')
          .style('width', size + 'px')
          .style('height', size + 'px')
          .style('left', (-size / 2) + 'px')
          .style('top', (-size / 2) + 'px')
          .on('animationend', function () { d3.select(this).remove(); });
      } else if (kind === 'release') {
        ghost.classed('press', false);
      } else if (kind === 'fade') {
        ghost.classed('on', false);
      } else if (kind === 'done') {
        cancelGhost();
        return;
      }
    }
    run.frame = requestAnimationFrame(ghostFrame);
  }

  function playGhost(d) {
    var hx = transform.applyX(d.x);
    var hy = transform.applyY(d.y);
    var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var dx = calm ? 0 : 110;
    var dy = calm ? 0 : 90;
    if (hx + dx > plot.width - 16) dx = -dx;
    if (hy + dy > plot.height - 16) dy = -dy;
    var sx = hx + dx;
    var sy = hy + dy;
    if (sx < 16) sx = 16;
    if (sy < 16) sy = 16;
    var len = Math.hypot(dx, dy) || 1;
    ghost.selectAll('.ring').remove();
    ghost.classed('press', false);
    ghost.style('transform', 'translate(' + sx + 'px,' + sy + 'px)');
    ghost.classed('on', true);
    ghostRun = {
      d: d,
      t0: performance.now(),
      sx: sx,
      sy: sy,
      nx: -dy / len,
      ny: dx / len,
      calm: calm,
      step: 0
    };
    ghostRun.frame = requestAnimationFrame(ghostFrame);
  }

  function queueGhost(d) {
    if (ghostRun && ghost.classed('on')) return;
    cancelGhost();
    ghostTimer = setTimeout(function () {
      ghostTimer = null;
      if (locked !== d) return;
      if (document.hidden) {
        ghostHold = d;
        return;
      }
      playGhost(d);
    }, GHOST_DELAY);
  }

  function onGhostVisible() {
    if (document.hidden) {
      if (ghostRun && ghostRun.frame) {
        cancelAnimationFrame(ghostRun.frame);
        ghostRun.frame = 0;
      }
      return;
    }
    if (ghostRun) {
      if (!ghostRun.frame) ghostRun.frame = requestAnimationFrame(ghostFrame);
      return;
    }
    var held = ghostHold;
    ghostHold = null;
    if (held && locked === held) playGhost(held);
  }

  document.addEventListener('visibilitychange', onGhostVisible);

  function onClick(event, d) {
    event.preventDefault();
    event.stopPropagation();
    if (swallowDismissTap()) return;
    if (event.shiftKey || event.ctrlKey || event.metaKey) toggleSelected(d);
    else setSelection([d.index]);
    if (locked) queueGhost(locked);
  }

  function onDblClick(event, d) {
    event.preventDefault();
    event.stopPropagation();
    cancelGhost();
    window.open(d.url, '_blank');
  }

  function showTip(d, event) {
    var authors = (d.authors || []).slice(0, 3).join(', ')
      + ((d.authors || []).length > 3 ? ' et al.' : '');
    var when = d.date
      ? d.date + (d.date_source && d.date_source !== 'arxiv-api'
          ? ' (' + d.date_source.replace('-', ' ') + ')' : '')
      : '';
    var hint = locked
      ? 'held \u00b7 shift-click adds \u00b7 double-click to open \u00b7 Esc to release'
      : 'click to hold \u00b7 shift-click to add \u00b7 double-click to open';
    var whoWhen = [authors ? escapeHtml(authors) : '', when]
      .filter(Boolean).join(' &middot; ');
    tip.html('<b>' + escapeHtml(d.title) + '</b>'
      + (whoWhen ? '<div class="meta">' + whoWhen + '</div>' : '')
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
    if (locked) {
      // Measure at the origin so the right edge cannot shrink the box.
      // Layout sizes, so the html.rotated turn does not swap them.
      tip.style('left', '0px').style('top', '0px');
      var el = tip.node();
      tipSize = { w: el.offsetWidth, h: el.offsetHeight };
      tipOffset = null;
      pinTip(d);
    } else {
      moveTip(event);
    }
  }

  var tipGrid = null;
  var tipSat = null;
  var tipStamp = null;
  var tipCols = 0;
  var tipRows = 0;

  function ensureTipGrid(cols, rows) {
    if (!tipGrid || tipCols !== cols || tipRows !== rows) {
      tipCols = cols;
      tipRows = rows;
      tipGrid = new Float64Array(cols * rows);
      tipSat = new Float64Array((cols + 1) * (rows + 1));
      tipStamp = new Int32Array(cols * rows);
      return;
    }
    tipGrid.fill(0);
  }

  function stampTipRect(x0, y0, x1, y1, weight) {
    if (!(x1 > x0 && y1 > y0)) return;
    var c0 = Math.max(0, Math.floor(x0 / TIP_CELL));
    var r0 = Math.max(0, Math.floor(y0 / TIP_CELL));
    var c1 = Math.min(tipCols, Math.ceil(x1 / TIP_CELL));
    var r1 = Math.min(tipRows, Math.ceil(y1 / TIP_CELL));
    var r, c, row;
    for (r = r0; r < r1; r += 1) {
      row = r * tipCols;
      for (c = c0; c < c1; c += 1) tipGrid[row + c] += weight;
    }
  }

  function fillTipSat() {
    var satW = tipCols + 1;
    var r, c, rowSum, gridRow, satRow, prevRow;
    for (r = 0; r < tipRows; r += 1) {
      rowSum = 0;
      gridRow = r * tipCols;
      satRow = (r + 1) * satW;
      prevRow = r * satW;
      for (c = 0; c < tipCols; c += 1) {
        rowSum += tipGrid[gridRow + c];
        tipSat[satRow + c + 1] = tipSat[prevRow + c + 1] + rowSum;
      }
    }
  }

  function areaCost(x, y, w, h) {
    var c0 = Math.floor(x / TIP_CELL);
    var r0 = Math.floor(y / TIP_CELL);
    var c1 = Math.floor((x + w - 1e-6) / TIP_CELL);
    var r1 = Math.floor((y + h - 1e-6) / TIP_CELL);
    if (c0 < 0) c0 = 0;
    if (r0 < 0) r0 = 0;
    if (c1 >= tipCols) c1 = tipCols - 1;
    if (r1 >= tipRows) r1 = tipRows - 1;
    if (c0 > c1 || r0 > r1) return 0;
    var satW = tipCols + 1;
    return tipSat[(r1 + 1) * satW + (c1 + 1)]
      - tipSat[r0 * satW + (c1 + 1)]
      - tipSat[(r1 + 1) * satW + c0]
      + tipSat[r0 * satW + c0];
  }

  function tipPlaceCost(x, y, w, h, hx, hy, rr) {
    var nx = hx < x ? x : (hx > x + w ? x + w : hx);
    var ny = hy < y ? y : (hy > y + h ? y + h : hy);
    var dist = Math.hypot(hx - nx, hy - ny);
    return areaCost(x, y, w, h) + TIP_DIST * Math.max(0, dist - rr - TIP_GAP);
  }

  function clampTipPos(x, y, minX, minY, maxX, maxY) {
    if (maxX >= minX) {
      if (x < minX) x = minX;
      else if (x > maxX) x = maxX;
    } else {
      x = 8;
    }
    if (maxY >= minY) {
      if (y < minY) y = minY;
      else if (y > maxY) y = maxY;
    } else {
      y = 8;
    }
    return [x, y];
  }

  function scanTip(minX, minY, maxX, maxY, w, h, hx, hy, rr) {
    if (maxX < minX || maxY < minY) return null;
    var best = null;
    var y = minY;
    var x, cost;
    while (y <= maxY) {
      x = minX;
      while (x <= maxX) {
        cost = tipPlaceCost(x, y, w, h, hx, hy, rr);
        if (!best || cost < best.cost) {
          best = { x: x, y: y, cost: cost };
          if (cost === 0) return best;
        }
        if (x === maxX) break;
        x += TIP_CELL;
        if (x > maxX) x = maxX;
      }
      if (y === maxY) break;
      y += TIP_CELL;
      if (y > maxY) y = maxY;
    }
    return best;
  }

  function stampTipLinks(inSel) {
    tipStamp.fill(0);
    var stampId = 1;
    var i, e, cpt, x0, y0, x1, y1, x2, y2, approx, steps, s, t, u, px, py, c, r, idx;
    for (i = 0; i < edges.length; i += 1) {
      e = edges[i];
      if (!inSel[e.source.index] && !inSel[e.target.index]) continue;
      cpt = edgeControl(e);
      x0 = transform.applyX(e.source.x);
      y0 = transform.applyY(e.source.y);
      x1 = transform.applyX(cpt.x);
      y1 = transform.applyY(cpt.y);
      x2 = transform.applyX(e.target.x);
      y2 = transform.applyY(e.target.y);
      approx = Math.hypot(x1 - x0, y1 - y0) + Math.hypot(x2 - x1, y2 - y1);
      steps = Math.max(1, Math.ceil(approx / 5));
      for (s = 0; s <= steps; s += 1) {
        t = s / steps;
        u = 1 - t;
        px = u * u * x0 + 2 * u * t * x1 + t * t * x2;
        py = u * u * y0 + 2 * u * t * y1 + t * t * y2;
        c = Math.floor(px / TIP_CELL);
        r = Math.floor(py / TIP_CELL);
        if (c < 0 || r < 0 || c >= tipCols || r >= tipRows) continue;
        idx = r * tipCols + c;
        if (tipStamp[idx] === stampId) continue;
        tipStamp[idx] = stampId;
        tipGrid[idx] += TIP_LINK;
      }
      stampId += 1;
    }
  }

  /* Cover selected disks and labels, then highlighted links and neighbour
     disks. Keep the previous offset while panning unless another spot is
     clearly cheaper. */
  function pinTip(d) {
    // showTip measures at 0,0. A later zoom frame must not remeasure in place.
    if (!tipSize || !(tipSize.w > 0 && tipSize.h > 0)) return;
    var w = tipSize.w;
    var h = tipSize.h;
    // plot.width/height rather than a live DOM read: this runs on every zoom
    // event and a layout flush here would be paid per pointer move.
    var cols = Math.max(1, Math.ceil(plot.width / TIP_CELL));
    var rows = Math.max(1, Math.ceil(plot.height / TIP_CELL));
    ensureTipGrid(cols, rows);

    var inSel = {};
    var ownLabel = null;
    selected.forEach(function (i) {
      inSel[i] = true;
      var n = nodes[i];
      var nsx = transform.applyX(n.x);
      var nsy = transform.applyY(n.y);
      var nrr = n.r * transform.k;
      var pad = ringPast(isHit(n.index)) + 2;
      stampTipRect(
        nsx - nrr - pad, nsy - nrr - pad, nsx + nrr + pad, nsy + nrr + pad,
        TIP_HIT
      );
      var label = selectedLabelBox(n);
      if (label) stampTipRect(label[0], label[1], label[2], label[3], TIP_HIT);
      if (n === d) ownLabel = label;
    });
    var seen = {};
    function stampNeighbour(j) {
      if (inSel[j] || seen[j]) return;
      seen[j] = true;
      var n = nodes[j];
      var nsx = transform.applyX(n.x);
      var nsy = transform.applyY(n.y);
      var nrr = n.r * transform.k;
      stampTipRect(nsx - nrr, nsy - nrr, nsx + nrr, nsy + nrr, TIP_LINK);
    }
    selected.forEach(function (i) {
      neighbours[i].inc.forEach(stampNeighbour);
      neighbours[i].out.forEach(stampNeighbour);
    });
    if (document.getElementById('edges').checked) stampTipLinks(inSel);
    fillTipSat();

    var hx = transform.applyX(d.x);
    var hy = transform.applyY(d.y);
    var rr = d.r * transform.k;
    var minX = 8;
    var maxX = plot.width - w - 8;
    var minY = plot.headerBottom + 4;
    var maxY = plot.height - h - 8;
    if (minY > maxY) minY = 8;

    var best = null;
    if (tipOffset) {
      var stuck = clampTipPos(
        hx + tipOffset.dx, hy + tipOffset.dy, minX, minY, maxX, maxY
      );
      best = {
        x: stuck[0],
        y: stuck[1],
        cost: tipPlaceCost(stuck[0], stuck[1], w, h, hx, hy, rr)
      };
    }
    var belowY = ownLabel ? ownLabel[3] + 6 : hy + rr + TIP_GAP;
    var spots = [
      [hx + rr + TIP_GAP, hy - 12],
      [hx - rr - w - TIP_GAP, hy - 12],
      [hx - w / 2, belowY],
      [hx - w / 2, hy - rr - h - TIP_GAP]
    ];
    var classic = null;
    spots.forEach(function (spot) {
      var p = clampTipPos(spot[0], spot[1], minX, minY, maxX, maxY);
      var cost = tipPlaceCost(p[0], p[1], w, h, hx, hy, rr);
      if (!classic || cost < classic.cost) {
        classic = { x: p[0], y: p[1], cost: cost };
      }
    });
    if (!best || classic.cost < best.cost - TIP_STICKY) best = classic;
    if (best.cost > TIP_STICKY) {
      var scanned = scanTip(minX, minY, maxX, maxY, w, h, hx, hy, rr);
      if (scanned && scanned.cost < best.cost - TIP_STICKY) best = scanned;
    }
    var left = Math.round(best.x);
    var top = Math.round(best.y);
    tip.style('left', left + 'px').style('top', top + 'px');
    tipOffset = { dx: left - hx, dy: top - hy };
  }

  function moveTip(event) {
    var pad = 14;
    var el = tip.node();
    var w = el.offsetWidth;
    var h = el.offsetHeight;
    // d3.pointer inverts the svg's screen matrix, which includes the
    // html.rotated body turn, so this is the pointer in the svg's own pixels.
    var at = d3.pointer(event, svg.node());
    var x = at[0] + pad;
    var y = at[1] + pad;
    if (x + w > plot.width - 8) x = at[0] - w - pad;
    if (y + h > plot.height - 8) y = at[1] - h - pad;
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

  var corpusState = 'idle';
  var searchTimer = null;

  function compileSlashQuery(trimmed) {
    var escaped = false;
    var i;
    for (i = 1; i < trimmed.length; i++) {
      var ch = trimmed.charAt(i);
      if (escaped) {
        escaped = false;
        continue;
      }
      if (ch === '\\') {
        escaped = true;
        continue;
      }
      if (ch !== '/') continue;
      var pattern = trimmed.slice(1, i);
      var flags = trimmed.slice(i + 1);
      if (!pattern) return null;
      if (!/^[dgimsuvy]*$/.test(flags)) {
        return {kind: 'lit', term: trimmed.toLowerCase()};
      }
      if (flags.indexOf('i') < 0) flags += 'i';
      try {
        return {kind: 're', re: new RegExp(pattern, flags)};
      } catch (err) {
        return {kind: 'lit', term: trimmed.toLowerCase()};
      }
    }
    return {kind: 'lit', term: trimmed.toLowerCase()};
  }

  function compileQuery(raw) {
    var trimmed = (raw || '').trim();
    if (!trimmed) return null;
    if (trimmed.charAt(0) === '/') return compileSlashQuery(trimmed);
    if (/[*?]/.test(trimmed)) {
      var glob = trimmed.toLowerCase()
        .replace(/[.+^${}()|[\]\\]/g, '\\$&')
        .replace(/\*/g, '.*')
        .replace(/\?/g, '.');
      return {kind: 're', re: new RegExp(glob)};
    }
    return {kind: 'lit', term: trimmed.toLowerCase()};
  }

  function textMatches(text, query) {
    if (!text) return false;
    if (query.kind === 'lit') return text.indexOf(query.term) >= 0;
    query.re.lastIndex = 0;
    return query.re.test(text);
  }

  function loadCorpus() {
    if (corpusState !== 'idle') return;
    var url = '';
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || '';
      if (src.indexOf('graph_data.js') < 0) continue;
      url = src.replace(/graph_data\.js(?=[?#]|$)/, 'fulltext_search.js');
      break;
    }
    if (!url) {
      corpusState = 'error';
      return;
    }
    corpusState = 'loading';
    var script = document.createElement('script');
    script.src = url;
    script.onload = function () {
      corpusState = window.FULLTEXT_SEARCH ? 'ready' : 'error';
      applyFilters();
    };
    script.onerror = function () {
      corpusState = 'error';
      applyFilters();
    };
    document.head.appendChild(script);
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
    var raw = document.getElementById('search').value;
    var query = compileQuery(raw);
    var termActive = Boolean(query);
    if (termActive) loadCorpus();
    var corpus = window.FULLTEXT_SEARCH || null;
    var citeOn = citeFilterOn();
    var tgOn = telegramFilterOn();
    var filtering = termActive || Boolean(tagFilter) || citeOn || tgOn;
    var key = filtering
      ? [raw, tagFilter || '', citeOn ? '1' : '', tgOn ? '1' : '',
         corpus ? '1' : ''].join('\0')
      : '';
    if (!filtering) {
      matches = null;
      hitSet = null;
      filterKey = '';
    } else if (key !== filterKey) {
      filterKey = key;
      matches = nodes.filter(function (d) {
        if (citeOn && !citesSeed[d.index]) return false;
        if (tgOn && !d.telegram) return false;
        if (tagFilter === 'untagged') {
          if (d.topic) return false;
        } else if (tagFilter && FIELD_SET[tagFilter]) {
          if (d.topic !== tagFilter) return false;
        } else if (tagFilter) {
          if ((d.ideas || []).indexOf(tagFilter) < 0
              && (d.tags || []).indexOf(tagFilter) < 0) {
            return false;
          }
        }
        if (termActive && !textMatches(d.haystack, query)
            && !(corpus && textMatches(corpus[d.id], query))) {
          return false;
        }
        return true;
      }).map(function (d) { return d.index; });
      hitSet = new Set(matches);
    }
    nodeSel.classed('dim', function (d) {
      return hitSet ? !hitSet.has(d.index) : false;
    });
    labelSel.classed('dim', function (d) {
      return hitSet ? !hitSet.has(d.index) : false;
    });
    styleNodeStrokes();
    var base = note(hitSet ? hitSet.size : null);
    var prefix = '';
    if (termActive && corpusState === 'loading') {
      prefix = 'loading full text\u2026  \u00b7  ';
    } else if (termActive && corpusState === 'error') {
      prefix = 'full-text index unavailable  \u00b7  ';
    }
    document.getElementById('note').textContent = prefix + base;
    if (locked) highlight();
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
    if (locked) highlight();
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
    if (locked) pinTip(locked);
  });
  document.getElementById('search').addEventListener('input', function () {
    if (corpusState === 'error') corpusState = 'idle';
    clearTimeout(searchTimer);
    searchTimer = setTimeout(applyFilters, 150);
  });
  document.getElementById('citefilter').addEventListener('change', function () {
    savePrefs();
    applyFilters();
  });
  document.getElementById('tgfilter').addEventListener('change', function () {
    savePrefs();
    applyFilters();
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
  // Phone drawer (html.compact): the header with the `open` class. Not
  // persisted, so a phone always starts with the map alone.
  var menuButton = document.getElementById('menu');
  function setDrawer(open) {
    var on = headerEl.classList.toggle('open', open);
    menuButton.setAttribute('aria-expanded', on);
    // Closing hides every control but the button; do not strand focus there.
    if (!on && headerEl.contains(document.activeElement)) menuButton.focus();
  }
  menuButton.addEventListener('click', function () {
    setDrawer(!headerEl.classList.contains('open'));
  });
  // Tapping the map means "I want to see it". That tap still produces a
  // click (d3-zoom only stops propagation), which must not also release the
  // held papers or select a disk.
  var dismissTap = false;
  svg.on('pointerdown.drawer', function () {
    dismissTap = headerEl.classList.contains('open');
    if (dismissTap) setDrawer(false);
  });
  function swallowDismissTap() {
    if (!dismissTap) return false;
    dismissTap = false;
    return true;
  }
  // The head script flips html.compact / html.rotated on media changes,
  // which need not come with a resize (pointer type, foldables).
  document.documentElement.addEventListener('modechange', function () {
    setDrawer(false);
    scheduleRedraw();
  });

  document.getElementById('reset').addEventListener('click', function () {
    unlock();
    setDrawer(false);
    svg.transition().duration(350).call(zoom.transform, d3.zoomIdentity);
  });
  svg.on('click', function (event) {
    if (swallowDismissTap()) return;
    if (event.target.tagName !== 'circle') unlock();
  });
  window.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (headerEl.classList.contains('open')) {
      setDrawer(false);
      return;
    }
    if (selected.length) {
      unlock();
      return;
    }
    document.getElementById('search').value = '';
    document.getElementById('citefilter').checked = false;
    document.getElementById('tgfilter').checked = false;
    tagFilter = null;
    markLegend();
    savePrefs();
    applyFilters();
  });

  var resizeTimer = null;
  function scheduleRedraw() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(redraw, 180);
  }
  window.addEventListener('resize', scheduleRedraw);

  buildLegend();
  syncAddCited();
  document.getElementById('stats').textContent = stats();
  document.getElementById('note').textContent = note(null);
  redraw();
  syncEdges();
  if (matches || tagFilter || citeFilterOn() || telegramFilterOn()) {
    applyFilters();
  }
  syncShareButton();
  applyHash(true);
}());
