---
name: Shareable selection links on the citation map
overview: Turn the map's single "held" paper into an ordered multi-selection (click = hold one, shift/ctrl-click = add/remove), mirror it into the URL fragment as `#sel=<key>,<key>` via `history.replaceState`, and restore it on load / `hashchange` with the view zoomed to the selected papers. A `copy link` button puts that URL on the clipboard. Pure front-end change in `src/map.js` + `src/index.html`; no pipeline or data rebuild, plus a Playwright check in `src/verify_map.py`.
todos:
  - id: selection-state
    content: "map.js: add `selected` (ordered indices), `byId`, `setSelection()`, `toggleSelected()`; route `lock`/`unlock`/`onClick`/Esc/reset through it"
    status: pending
  - id: multi-highlight
    content: "map.js: generalise `highlight`, `styleEdges`, `restyleForZoom`, `placeLabels` from `locked` to all selected nodes (`focusIndices()`)"
    status: pending
  - id: hash-sync
    content: "map.js: `encodeKey`/`selectionHash`/`parseHash`/`applyHash`/`syncHash`; call `applyHash(true)` after the first `redraw()` and on `hashchange`"
    status: pending
  - id: focus-view
    content: "map.js: `focusSelection()` zooms/pans (`svg.transition().call(zoom.transform, …)`) to the bbox of the selected nodes, capped at `FOCUS_MAX_K`"
    status: pending
  - id: share-button
    content: "index.html + map.js: `#share` button (`copy link`, disabled when nothing selected) writing the URL to the clipboard; update hints (`shift-click to add`)"
    status: pending
  - id: verify
    content: "verify_map.py: deep-link block before `browser.close()` (hashchange path, reload path, shift-click grows hash, Esc clears, unknown key ignored, copy link)"
    status: pending
  - id: readme-note
    content: "readme.md line 7: one clause explaining `#sel=<key>,…` / the copy-link button"
    status: pending
  - id: run-checks
    content: "Run `node --check src/map.js`, `python src/verify_map.py`, manual check over `python -m http.server`; `git diff --stat` shows only the four files"
    status: pending
isProject: false
---

# Shareable selection links on the citation map

## Goal

A user selects one or more papers on the live map (GitHub Pages `https://vinnik-dmitry07.github.io/favorite-papers/` or local `src/index.html`), presses **copy link** (or copies the address bar, which is kept in sync), and sends the URL. Whoever opens it lands on the map with exactly those papers selected (rings, forced labels, pinned tooltip on the last one, unrelated nodes dimmed) and the viewport zoomed/panned so the selection fills the plot.

URL shape (fragment, so nothing changes server-side and GitHub Pages / `python -m http.server` / Playwright's server all work):

```text
https://vinnik-dmitry07.github.io/favorite-papers/#sel=arxiv:2407.21783,arxiv:2501.00656
http://localhost:8000/src/index.html#sel=doi:10.1038/s41586-023-06924-6
```

`<key>` is the node id already in `assets/graph_data.js` (`d.id`), i.e. the readme key produced by `classify()` in `src/common.py` (`arxiv:…`, `doi:…`, `openreview:…`, `acl:…`, `url:<slug>`). It is also what `filter/report.md` anchors and `scores.csv` use, so a link can be built from a readme bullet without opening the map.

## Assumptions

Inferred from `src/map.js` (1363 lines, IIFE, ES5 style, d3 v7), `src/index.html`, `src/verify_map.py`, `.github/workflows/pages.yml`, `assets/graph.json`; the implementer may rely on all of these.

- **Selection does not exist yet; only a single "hold".** `locked` (one node) is set by `onClick → lock(d)`, cleared by `unlock()` from the svg background click, `Escape`, and `#reset`. Search/legend/checkbox filters produce `matches` (a filter, not a selection). There is no URL/hash/`history` code anywhere in `src/` (grep for `location.hash|URLSearchParams|history.|hashchange|clipboard` returns nothing). Preferences (`labels`, `yaxis`, checkboxes, `tag`) live in `localStorage` under `key-papers-map-prefs`; selection must **not** go there, the URL is its carrier.
- **Node ids are unique and fragment-safe.** 383 nodes, 383 distinct `id`s (300 `arxiv`, 57 `url`, 14 `doi`, 8 `openreview`, 4 `acl`); max length 132. None contains `,`, `&`, `#`, `%`, `;`, `+` or whitespace; exactly one contains `?` (`url:papers.ssrn.com/sol3/papers.cfm?abstract_id=5239006`); `doi:` and `url:` ids contain `/`, one `url:` id contains `~`. Comma is therefore a safe separator and `:` `/` `?` `~` can stay literal (RFC 3986 allows them in a fragment), keeping links readable.
- **Positions are base-space; the view is one d3 zoom transform.** After `layout()`, each node has `d.x`, `d.y`, `d.r` in untransformed SVG units; screen = `transform.applyX(d.x)`. `zoom = d3.zoom().scaleExtent([0.55, 9])`; `svg.call(zoom.transform, t)` (optionally through `svg.transition()`) is how `#reset` and `applyYAxis` set the view, and the `zoom` handler already refreshes axes, strokes, `pinTip(locked)` and labels. `plot` has `top/bottom/left/right/timeLeft/width/height` after `layout()`.
- **Startup order** at the bottom of `map.js`: `buildLegend(); syncAddCited(); stats/note; redraw(); syncEdges(); applyFilters() if filtering`. `redraw()` = `layout() → redrawAxes() → render()`; `render()` (re)binds `nodeSel`, `edgeSel`, `labelSel` with `.join`, reusing existing `<g>` elements, so classes survive a redraw; resize triggers `redraw()` after 180 ms; changing the y-axis resets the transform to identity (selection should survive, the focus zoom need not).
- **Highlight plumbing** to generalise: `related(d)` (self + in/out neighbours), `highlight(d)` (sets `.dim`/`.held`, `styleEdges()`, raises), `focused()` (`locked || hovered`), `styleEdges()` (in/out colours relative to the one focused node), `restyleForZoom()` (held ring stroke by `locked.index`), `placeLabels()` (`forced` = focus + neighbours + `matches`, `focusing` mode hides other labels), `clearHighlight()`. Tooltip: `showTip(d, event)` calls `pinTip(d)` when `locked` is set (event unused), `moveTip(event)` otherwise. `enter()` is a no-op while `locked` — keep that (hover stays off while a selection exists).
- **Deployment copies files verbatim.** `pages.yml` runs `sed 's|\.\./assets/|assets/|g' src/index.html > site/index.html`, `cp src/map.js site/`, `cp assets/graph_data.js`; so the feature ships on the next push to `main` with no workflow change. Locally the readme says `python -m http.server` from the repo root; `verify_map.py` serves `ROOT` on a random port and opens `/src/index.html` with Playwright + Chrome (`channel='chrome'`), collecting every `console.error`/`console.warning`/`pageerror` as a failure — so **never `console.warn` on unknown keys**.
- No data rebuild is needed: `graph_data.js`, `catalog.json`, scores, readme bullets are untouched. `assets/preview.png` does not change (no selection in the default view), so `--preview` is unnecessary.
- Tooling present: Node v24 (`node --check`), Python Playwright with Chrome (used by `verify_map.py`). Windows/PowerShell: run scripts, no heredocs; set `$env:PYTHONIOENCODING='utf-8'` before `verify_map.py` (its output has non-ASCII).

## Changes

### `src/map.js`

Keep the existing ES5 style (`var`, `function`, single quotes). All edits are inside the IIFE.

1. **State and lookup** — next to `var hovered = null, locked = null, matches = null, tagFilter = null;` (≈L329) add:

   ```js
   var selected = [];   // ordered node indices; the last one is the held paper (locked)
   var byId = {};
   nodes.forEach(function (d) { byId[d.id] = d.index; });
   var HASH_KEY = 'sel';
   var FOCUS_MAX_K = 4;    // never zoom tighter than this when focusing a selection
   var FOCUS_PAD = 70;     // screen px kept free around the selection bbox
   ```

   Helpers (place after `related()`):

   ```js
   function isSelected(i) { return selected.indexOf(i) >= 0; }
   function sameList(a, b) { /* same length and same order */ }
   function focusIndices() {
     if (selected.length) return selected;
     return hovered ? [hovered.index] : [];
   }
   function setSelection(indices) {
     selected = indices.slice();
     locked = selected.length ? nodes[selected[selected.length - 1]] : null;
     hovered = null;
     if (locked) {
       highlight(locked);
       showTip(locked, null);   // locked is set, so showTip → pinTip; event unused
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
   ```

   Rewire the existing functions rather than duplicating them: `lock(d, event)` → `setSelection([d.index])` (drop the `event` use); `unlock()` → `if (!locked && !selected.length) return; setSelection([]);`; `onClick(event, d)` → `event.preventDefault(); event.stopPropagation(); if (event.shiftKey || event.ctrlKey || event.metaKey) toggleSelected(d); else lock(d);`. `Escape` handler: first branch becomes `if (locked || selected.length) { unlock(); return; }`. `#reset` keeps calling `unlock()` (existing behaviour: reset view also releases the hold — now the selection too — and the hash is cleared by `syncHash`; if the user later prefers "reset zoom, keep selection", drop that one `unlock()` call). Background `svg.on('click')` unchanged (calls `unlock`).

2. **Multi-node highlight** — replace `locked`-specific logic with `focusIndices()` / `isSelected()`:
   - `highlight(d)`: focus set = union of `related(nodes[i])` over `focusIndices()` when non-empty, else `related(d)` (hover path). `.held` → `isSelected(n.index)`. Raise edges touching any focus index and every focus node (loop, not `d` only). Keep the `matches` dimming (`hit`) as is.
   - `styleEdges()`: `var focus = focusIndices(); if (!focus.length) { …default… return; }`; build `var inFocus = {}` from it; stroke: `inFocus[e.target.index] ? 'var(--in)' : inFocus[e.source.index] ? 'var(--out)' : 'var(--edge)'`; opacity/width by `inFocus[e.source.index] || inFocus[e.target.index]`.
   - `restyleForZoom()`: stroke `isSelected(d.index) ? 'var(--in)' : '#fff'`, width `(isSelected(d.index) ? 2.4 : 1.3) / transform.k`; keep `if (locked) pinTip(locked)`.
   - `placeLabels()`: `var focus = focusIndices();` → for each index mark it and its `inc`/`out` neighbours in `forced`; `var focusing = focus.length > 0 || Boolean(matches);`; the `if (!blocked || d === focus)` override becomes `if (!blocked || inFocus[d.index])`; the trailing `if (focus) visible[focus.index] = true;` becomes `focus.forEach(function (i) { visible[i] = true; });`. `focused()` can stay for `pinTip`/tooltip use or be deleted if no longer referenced.
   - `redraw()`: after the existing `applyFilters()` branch add `if (locked) highlight(locked);` so a resize / y-axis change re-applies dimming and the pinned tooltip for the whole selection.

3. **URL fragment sync** (new block, after the helpers above):

   ```js
   function encodeKey(id) {
     // encodeURI keeps : / ? ~ = readable; only the separator and fragment-breaking chars are escaped
     return encodeURI(id).replace(/[,&#]/g, function (c) { return encodeURIComponent(c); });
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
     try { window.history.replaceState(null, '', url); } catch (err) { return; }
   }
   function parseHash(hash) {
     // '#sel=a,b&other=…' → node indices (unknown / duplicate keys dropped, bare arXiv ids accepted)
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
       if (idx != null && out.indexOf(idx) < 0) out.push(idx);
     });
     return out;
   }
   function applyHash(focus) {
     var indices = parseHash(window.location.hash);
     if (sameList(indices, selected)) return;
     setSelection(indices);            // re-canonicalises the hash (drops unknown keys)
     if (focus && indices.length) focusSelection();
   }
   window.addEventListener('hashchange', function () { applyHash(true); });
   ```

   `replaceState` (not `pushState`) so clicking around does not spam history and does not fire `hashchange`. Startup: after the final `redraw(); syncEdges(); if (…) applyFilters();` lines add `syncShareButton(); applyHash(true);` — positions exist by then, so `highlight` and `focusSelection` are safe.

4. **Focus the view on the selection**:

   ```js
   function focusSelection() {
     if (!selected.length || !plot.width) return;
     var x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
     selected.forEach(function (i) {
       var d = nodes[i];
       x0 = Math.min(x0, d.x - d.r); x1 = Math.max(x1, d.x + d.r);
       y0 = Math.min(y0, d.y - d.r); y1 = Math.max(y1, d.y + d.r);
     });
     var extent = zoom.scaleExtent();
     var vw = plot.right - plot.timeLeft, vh = plot.bottom - plot.top;
     var k = Math.min(FOCUS_MAX_K,
                      (vw - 2 * FOCUS_PAD) / Math.max(x1 - x0, 1),
                      (vh - 2 * FOCUS_PAD) / Math.max(y1 - y0, 1));
     k = Math.max(extent[0], Math.min(extent[1], k));
     var tx = (plot.timeLeft + plot.right) / 2 - k * (x0 + x1) / 2;
     var ty = (plot.top + plot.bottom) / 2 - k * (y0 + y1) / 2;
     svg.transition().duration(500)
       .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(k));
   }
   ```

   The transition drives the existing `zoom` handler (axes, strokes, `pinTip(locked)`, labels) every frame, exactly like `#reset`. Only `applyHash(true)` calls it — interactive clicks never move the view.

5. **Share button + hints**:

   ```js
   function syncShareButton() {
     var button = document.getElementById('share');
     if (!button) return;
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
   ```

   Tooltip `hint` strings in `showTip`: locked → `'held \u00b7 shift-click adds \u00b7 double-click to open \u00b7 Esc to release'`; unlocked → `'click to hold \u00b7 shift-click to add \u00b7 double-click to open'`. Update the header comment at the top of the file with one line: selection is mirrored into `#sel=<key>,…` and restored on load.

### `src/index.html`

- In `.controls`, after `<button id="reset">reset view</button>` add
  `<button id="share" title="Copy a link that opens the map with the selected papers" disabled>copy link</button>`.
- CSS next to `button:hover`: `button:disabled { color: var(--muted); cursor: default; }` and `button:disabled:hover { border-color: var(--rule); }`.
- `.key` third span: `click to hold &middot; shift-click to add &middot; double-click to open`.
- Nothing else; `pages.yml`'s `sed` only touches `../assets/` paths.

### `src/verify_map.py`

Add a `deep_link` block right before `browser.close()` (after the narrow-viewport checks), so the rest of the suite is unaffected:

Note: `main()` reuses the name `target` for the hover coordinates dict (≈L192), so take the page URL from `map_url(server)` again.

```python
page.set_viewport_size({'width': 1440, 'height': 860})
page.select_option('#yaxis', 'cited')
page.wait_for_timeout(600)
base_url = map_url(server)
seeds = 'arxiv:2407.21783,arxiv:2501.00656'          # Llama 3, OLMo 2 — also SEED_IDS in map.js
page.goto(f'{base_url}#sel={seeds},arxiv:0000.00000')  # same-document → hashchange path; last key unknown
page.wait_for_timeout(1200)
linked = page.evaluate('''() => ({
    held: [...document.querySelectorAll('.nodes g.held')].map(g => g.__data__.id),
    dimmed: document.querySelectorAll('.nodes g.dim').length,
    k: d3.zoomTransform(document.getElementById('map')).k,
    hash: location.hash,
    tip: getComputedStyle(document.getElementById('tip')).opacity,
    share: document.getElementById('share').disabled,
})''')
print('deep link:', linked)
# expect: held == both seeds (order kept), hash == '#sel=' + seeds (unknown key dropped),
# k > 1, dimmed >= 200, tip opacity '1', share enabled
page.reload(wait_until='load')                          # load path keeps the fragment
page.wait_for_timeout(1500)
# re-evaluate the same object; same expectations, plus k > 1 again
page.evaluate('''() => { window.__copied = null;
    navigator.clipboard.writeText = (t) => { window.__copied = t; return Promise.resolve(); }; }''')
page.click('#share')
page.wait_for_timeout(200)
# expect window.__copied endswith '#sel=' + seeds and button text == 'copied'
third = page.evaluate('''() => {            // first bright, unselected, on-screen node (below the header)
    const g = [...document.querySelectorAll('.nodes g')].find(g => {
        if (g.classList.contains('held') || g.classList.contains('dim')) return false;
        const b = g.querySelector('circle').getBoundingClientRect();
        return b.y > 260 && b.y < innerHeight - 80 && b.x > 80 && b.x < innerWidth - 80;
    });
    const b = g.querySelector('circle').getBoundingClientRect();
    return {id: g.__data__.id, x: b.x + b.width / 2, y: b.y + b.height / 2};
}''')
page.keyboard.down('Shift')                             # page.mouse.click has no modifiers argument
page.mouse.click(third['x'], third['y'])
page.keyboard.up('Shift')
page.wait_for_timeout(300)
# expect 3 held and location.hash to end with ',' + third['id'] (unencoded for arxiv keys)
page.keyboard.press('Escape')
page.wait_for_timeout(300)
# expect 0 held, location.hash == '', share disabled
```

Bright unselected nodes exist because `highlight()` keeps the neighbours of the selected papers undimmed (Llama 3 / OLMo 2 are cited by dozens of entries). The 1200 ms wait covers the 500 ms focus transition. Each expectation appends to `errors` in the existing style; take a screenshot `09-deep-link.png` into `SHOTS`.

### `readme.md` (line 7, prose only)

After `[->live map<-](https://vinnik-dmitry07.github.io/favorite-papers/)` insert: `(select papers — shift-click adds — and press *copy link*, or append `#sel=arxiv:2407.21783,doi:10.1038/s41586-023-06924-6` with the readme keys)`. No bullets touched: `parse_readme.iter_bullets()` only reads `- ` lines and their continuations, and `collect_readme.readme_line_index()` splits line 7 on `](` and keeps the text before the first `)`, so the existing `https://vinnik-dmitry07.github.io/favorite-papers/` key is unchanged and the `#sel=…` example (placed after that `)`) creates no new key. Outputs of both scripts stay identical.

## Verification

```powershell
node --check src/map.js                    # syntax
$env:PYTHONIOENCODING='utf-8'
python src/verify_map.py                   # full Playwright suite incl. the new deep-link block; must end with "no console errors"
git diff --stat                            # exactly src/map.js, src/index.html, src/verify_map.py, readme.md
```

Manual (local server, repo root):

```powershell
python -m http.server 8000
```

- Open `http://localhost:8000/src/index.html#sel=arxiv:2407.21783,arxiv:2501.00656`: both nodes ringed and labelled, tooltip pinned on OLMo 2, view zoomed to them (k ≤ 4), other nodes dimmed.
- Shift-click a third node: ring added, address bar hash grows; plain click another node: selection collapses to that one; `copy link` → paste into a new tab → same state restored; `Esc` → hash removed, nothing selected; browser back/forward do not accumulate entries.
- Change `y:` axis and resize the window with a selection: selection and rings persist (view resets to identity on axis change, as before).
- Bad link `#sel=arxiv:0000.00000` → nothing selected, no console warning.
- `git status` afterwards: no new files in the repo; nothing committed.

## Open questions

none
