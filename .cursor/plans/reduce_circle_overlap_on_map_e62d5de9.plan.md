---
name: Reduce circle overlap on map
overview: Decouple circle size from the y-axis (size = in-list cited-by everywhere) and give the collision pass room to work (adaptive y nudge, small x nudge, stronger collide), then guard overlap with a per-mode check in verify_map.py.
todos:
  - id: size-rule
    content: "applyMetric(): radius from in-list cited-by (Litmaps count on citations axis) in every mode; note() states the size rule"
    status: completed
  - id: layout-freedom
    content: "layout(): per-node bounds (x ±12, adaptive y nudge ≤35% of row gap, quality ±12), weaker x/y forces, collide 0.85 x3, bounds as a per-tick force"
    status: completed
  - id: verify-overlap
    content: "verify_map.py: overlap_pairs() after each y-mode switch, fail above 50 pairs"
    status: completed
  - id: regen
    content: Run verify_map.py --preview, check shots and pair counts
    status: completed
isProject: false
---

# Reduce circle overlap on map

## Measured problem (browser, 1440x860, overlapping pairs after layout)

- cited 36 pairs, median r 6 — acceptable baseline
- cites 216, parents 518, children 471, bonus 163 — median r ~9.5, 150–180 circles with r > 10
- quality 919 — median r 16 (radius currently follows `q + 1`)
- citations 9

Two causes in [src/map.js](src/map.js):

1. `applyMetric()` sizes the circle by the same value as the y-axis. Cites counts are dense (row `refs=1` holds 57 papers, rows 2–4 hold ~37 each, 149 of 268 citing papers are dated 2025–26 so they share ~200 px of x), and quality is centred so nearly every node gets a big radius.
2. `layout()` gives the collision pass almost no freedom: `forceX 0.92`, `forceY 0.96`, `forceCollide 0.4` with 2 iterations, then a fixed post-clamp `d.y in [ty - 6, ty + 10]` and no x clamp at all (x barely moves because the force is so strong). Row gaps are 20–48 px, so ±6/10 px cannot spread 30 circles that need 2–3 sub-rows.

## 1. Size = in-list cited-by in every mode — `applyMetric()` in `src/map.js`

- Add `sizeValue(d)`: `yMode() === 'citations' ? (d.lit_cites || 0) : d.cites`.
- `radius = d3.scaleSqrt().domain([0, d3.max(nodes, sizeValue) || 1]).range([4, 21])`; `d.r = radius(sizeValue(d))` for all modes, including quality (drop the `q + 1` radius branch).
- Keep `maxY = d3.max(nodes, yCount)` for the y scale in count modes; keep `d.score` label priority as is (count modes: `yv*2 + …`; quality: `(q+1)*2 + (cites+refs)*0.5`).
- Footer `note()`: append `size: cited by on this list` when `yMode()` is not `cited`/`citations` so the size rule is stated when it differs from the axis. Update the header comment at the top of `map.js`.

## 2. Let collide actually separate circles — `layout()` in `src/map.js`

- Per-node allowed box computed before the simulation:
  - dated nodes: `dxMax = 12` px (about one month on the 11-year axis); undated keep the gutter `lo/hi`.
  - count modes, `yv > 0`: `up = clamp(0.35 * (ty - yRow(yv + 1)), 6, 16)`, `down = clamp(0.35 * (yRow(yv - 1) - ty), 6, 16)` where `yRow(v) = yBase(yEncode(v))` and `yRow(0)` is `plot.zeroRule`. A node never crosses the midpoint to the neighbouring row, so rows stay readable; upper sparse rows automatically get the small nudge they have today.
  - quality mode: `up = down = 12` px (≈0.05 score units on the ~500 px band; the tooltip shows the exact value).
  - zero / n/a band: keep the current `-6 / +10`.
- Forces: `forceX` 0.92 → 0.55, `forceY` 0.96 → 0.6, `forceCollide(r + 1.2)` strength 0.4 → 0.85, iterations 2 → 3, 300 ticks unchanged.
- Replace the single post-clamp with a custom `bounds` force run every tick (clamp `d.x`/`d.y` into the box and zero the velocity component when clamped), so collide resolves within the allowed box instead of being undone at the end. Keep the final `plot.top/bottom` clamp.

## 3. Regression guard — `src/verify_map.py`

- Add `overlap_pairs(page)` helper (same JS used for the measurement: pairs with `dist < r1 + r2 - 0.5`, plus median r) and call it after every `#yaxis` switch (`cited`, `cites`, `parents`, `children`, `bonus`, `citations`, `quality`), printing `mode: pairs N, median r`.
- Error if any mode has more than 50 overlapping pairs. Layout is deterministic (hash wobble, seeded d3 collide), so the threshold is stable.
- Existing checks stay valid: the hover test still picks the biggest node (DeepSeekMath, cited mode unchanged); `moved` counts stay well above thresholds because y positions are still metric-driven.

## 4. Regenerate

- No data rebuild (graph unchanged). `python src/verify_map.py --preview` refreshes `shots/*.png` and `assets/preview.png`; inspect the quality and cites shots for stray overlaps and confirm all modes report ≤ 50 pairs (target ≤ 20).

## Out of scope

Colour-by-quality toggle, readme, filter scores, commit.