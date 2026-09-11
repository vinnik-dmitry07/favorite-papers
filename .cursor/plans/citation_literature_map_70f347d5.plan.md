---
name: Citation literature map
overview: Build a Litmaps-style interactive map of every paper and blog in readme.md. Edges and the Y-axis come from references we extract ourselves (arXiv HTML first, then page links for blogs), not from Litmaps. Nodes stay a single color for now.
todos:
  - id: catalog
    content: Parse readme.md into map/catalog.json (all papers + blogs, dates/authors where available)
    status: completed
  - id: fetch-refs
    content: Fetch arXiv HTML (and blog HTML); extract bibliography + in-page paper links; cache under map/cache/
    status: completed
  - id: build-graph
    content: Match refs to catalog; write map/graph.json with in-corpus citation counts and edges
    status: completed
  - id: viz
    content: Build Litmaps-style D3 map (time x citations, curved edges, no topic colors)
    status: completed
  - id: readme-gitignore
    content: Gitignore map/cache/; link the local map from readme.md
    status: completed
isProject: false
---

# Litmaps-style citation map

## What you get

A local interactive map that mirrors [map.png](map.png): **time on X**, **citation impact on Y**, curved citation edges, Author/year labels on the important nodes. Unlike Litmaps, the graph is built only from references we parse out of the documents.

- Source of nodes: every list entry in [readme.md](readme.md) (~300 papers, blogs, repos, books). Telegram badges are ignored.
- No topic/section colors (your call). A later pass can add section pies.
- Y-axis: **in-corpus incoming citations** (how many *other listed items* cite this one). That stays consistent with “our own retrieval.” A Semantic Scholar global-count toggle is out of scope unless you ask for it later.
- Deliverable: open `map/index.html` in a browser. Optional one-line link at the top of the readme next to the existing Litmaps screenshot; keep the Litmaps URLs.

```mermaid
flowchart LR
  readme[readme.md]
  catalog[map/catalog.json]
  cache[map/cache HTML]
  graph[map/graph.json]
  viz[map/index.html]
  readme --> catalog
  catalog --> cache
  cache --> graph
  catalog --> graph
  graph --> viz
```

## 1. Catalog: parse the list

New script `map/parse_readme.py` walks [readme.md](readme.md) bullets and writes `map/catalog.json`.

Each node:

- `id`: arXiv id when present, otherwise a stable URL slug
- `title`, `section`, `urls`, `kind` (`arxiv` / `blog` / `openreview` / `doi` / `other`)
- `authors`, `date`: from [papers_titles.json](papers_titles.json) for known arXiv ids; arXiv API for missing ids (same pattern as [fetch_titles.py](fetch_titles.py)); for blogs, `<time>`, `article:published_time`, or a date in the URL (`/posts/2023-06-23-...`)
- Undated items stay in the catalog and sit in a small “date unknown” gutter on the left so they are not dropped

Reuse existing title/author data; do not depend on `result.json`.

## 2. Retrieve references (HTML-first)

New script `map/fetch_refs.py` with **console progress** (`12/280 fetching 2503.20783 ...`). Cache raw HTML under `map/cache/` (gitignored). Resume-friendly.

**arXiv papers** (preferred path you asked for):

1. `https://arxiv.org/html/{id}`
2. Fallback `https://ar5iv.labs.arxiv.org/html/{id}`
3. If both 404, record `html: false` and continue (node stays; it can still be *cited*)

From the HTML, extract outgoing refs by:

- Bibliography: `ltx_bibliography` / `ltx_bibitem` (arXiv HTML / LaTeXML)
- Every `arxiv.org/abs|pdf|html` link in the page (body + bib)
- DOI / OpenReview / other catalog URLs
- Bibitem title text for fuzzy match when there is no link

**Blogs and other HTML pages:** fetch the primary URL, collect the same link types plus any obvious references section. A Lilian Weng post that links `arxiv.org/abs/2301.04104` becomes an edge to DreamerV3 if that paper is in the catalog.

No PDF parsing in this pass.

## 3. Match refs and build the graph

New script `map/build_graph.py` writes `map/graph.json` (this file **is** committed so the map opens offline).

Match an extracted ref to a catalog node, in order:

1. Exact arXiv id
2. Exact catalog URL (normalized)
3. Normalized title similarity (punctuation stripped, `SequenceMatcher` / token overlap, high threshold ~0.88)

Edge `A -> B` means **A cites B**. Only keep edges where both ends are in the catalog. Node `citations` = in-degree. Print a short coverage summary: HTML found, refs extracted, edges matched, unmatched-ref count.

## 4. Visualization (Litmaps layout, no colors)

Self-contained [map/index.html](map/index.html) + [map/map.js](map/map.js) (D3 from CDN). Load `graph.json`.

| Litmaps cue | Our version |
|---|---|
| X = more recently published | Linear date axis |
| Y = more citations | `log1p(in-corpus citations)` |
| Node size ~ impact | Radius from the same count (floor so 0-cite nodes stay visible) |
| Topic pies / legend | **Omitted** — one fill color |
| Author, year labels | First author + year; only top-cited / high-degree nodes labeled to avoid 300-label soup |
| Curved citation edges | Low-opacity cubic curves; fade unless a node is hovered |
| Hover / click | Tooltip: title, authors, date, in-corpus cites, section (text only); click opens the primary URL |

Also: zoom/pan, search box, “highlight neighbors,” edge on/off. Positions are data-driven (date, citations) plus a tiny jitter so coincident dates do not stack. Not a force layout.

## 5. Repo hygiene

- Add `map/cache/` to [.gitignore](.gitignore)
- Commit `map/catalog.json`, `map/graph.json`, and the viz files
- `python map/fetch_refs.py` then `python map/build_graph.py` to rebuild after the readme grows

## Out of scope (unless you want them next)

- Section / LLM topic colors and pie nodes
- Semantic Scholar / OpenAlex global citation counts
- Adding papers that are cited but **not** on the list
- Replacing or recreating the hosted Litmaps links
