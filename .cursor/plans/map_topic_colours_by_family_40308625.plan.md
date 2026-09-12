---
name: Map topic colours by family
overview: Recolour the 23 map fields so each of the 9 families owns a distinct hue and fields inside a family differ by shade, then group the legend chips by family and regenerate the graph data and preview.
todos:
  - id: palette
    content: Replace hex column of FIELDS in src/topics.py with the family-hue palette
    status: completed
  - id: legend
    content: Group legend chips by family in map.js buildLegend() and add .legend .fam style in index.html
    status: completed
  - id: rebuild
    content: Run src/build_graph.py, confirm 383 nodes and new colours in assets/graph_data.js
    status: completed
  - id: contrast
    content: Run a temp pairwise-dE / alpha-wash check from %TEMP%, tune hexes, rebuild
    status: completed
  - id: preview
    content: Run src/verify_map.py --preview, inspect assets/preview.png and hover shot
    status: completed
isProject: false
---

# Map topic colours by family

## Problem

`FIELDS` in [src/topics.py](src/topics.py) claims "families share a hue", but the hex values do not follow it. Hue audit of the current palette:

- 136–191° (green/teal): Optimizers, Continual, Scaling, Open-ended, NeuroAI, RLVR, SSL, Deep RL — 8 fields from 6 families
- 10–28° (red/orange/brown): Safety, Harness, Self-improve, Latent, Reasoning — 5 fields from 3 families
- 231–264° (indigo/violet): Architectures, Inter-model, Diffusion, Interp — 2 families
- Unused: blue ~215°, gold/olive 40–90°, magenta/pink 300–340° are almost empty

Colours flow `topics.py FIELDS` -> `taxonomy()` -> `build_graph.py` -> `assets/graph_data.js` -> `map.js topicColor()` / `buildLegend()`. Nothing else stores colours, so the fix is one table plus a legend tweak and a rebuild.

## 1. New palette in `src/topics.py`

Keep names, families and order; replace only the hex column. One hue per family, ~40° apart, lightness 35–60% on the `#fbfbfa` background; inside a family the largest field gets the mid shade, others go darker/lighter (and a small ±10° hue nudge when a family has 3–4 fields so shades survive the `fill-opacity: 0.4` wash on zero-count nodes).

Draft (exact hexes tuned in step 4):

- RL, blue ~215°: RLVR `#3d7fd6` (57 papers, mid), Deep RL `#1e3f7a` (navy)
- Reasoning, orange ~30°: Reasoning `#e8891f`, Latent `#a4501a` (burnt)
- Models, violet ~265°: Architectures `#7d5cc9`, Inter-model `#4b3792` (dark), Diffusion `#b58fe6` (light)
- Training, green ~130°: Dynamics `#43a047` (26, mid), Optimizers `#1b5e20` (dark), Continual `#7cb342` (yellow-green), Scaling `#a5d6a7` (light mint)
- Agents, teal ~178°: Harness `#0b6b66` (dark), Self-improve `#1fa89e` (mid), Open-ended `#77d4c6` (light), Discovery `#36858f` (slate-teal)
- Understanding, magenta ~320°: Interp `#c2408a`, Repr `#e18fc0` (light)
- Mind, red ~5°: Safety `#d43d3d`, Consciousness `#8e1d3c` (wine), NeuroAI `#ef8c78` (coral)
- SSL, olive ~65°: `#8a9a1e`
- Other: Finance `#8d8578` (warm taupe, away from blue), Other `#9aa3ab` (unchanged; also `UNTAGGED` in map.js)

## 2. Legend grouped by family — `src/map.js`, `src/index.html`

In `buildLegend()` (map.js ~L801) keep the single wrapping `fields` row but iterate `taxonomy.fields` grouped by `field.family` (already present in the data), inserting a small uppercase family label before each group; unknown `extraFields` stay at the end. Add a `.legend .fam` style next to `.legend-label` in index.html (10px, uppercase, muted, left margin). The `all` / `untagged` chips and click-to-filter behaviour are untouched.

## 3. Regenerate derived files

```powershell
python src/build_graph.py            # assets/graph.json, assets/graph_data.js (taxonomy colours)
python src/verify_map.py --preview   # refreshes assets/preview.png, checks fills >= 5 and legend chips
```

Node/edge counts must not change (383 nodes). The current `preview.png` is stale (old tag taxonomy), so it gets refreshed as a side effect.

## 4. Verify contrast

Temporary script under `%TEMP%` (not in the repo): sRGB -> Lab, print pairwise CIE76 dE for all 23 fields, flag any cross-family pair below ~20 and any within-family pair below ~12; also print every colour at 0.4 alpha over `#fbfbfa` and check dark shades do not collapse onto a light sibling. Adjust hexes until clean, rerun step 3, then look at `assets/preview.png` and the hover shot from `verify_map.py`.

If zero-count nodes still wash dark shades into light siblings, raise `fill-opacity` for `yCount(d) == 0` in `render()` (map.js ~L492) from 0.4 to ~0.55 — optional, only if the preview shows the problem.

## Out of scope

No changes to field assignment rules, ideas, readme, filter scores; no commit.