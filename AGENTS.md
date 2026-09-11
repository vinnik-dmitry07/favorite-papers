# AGENTS.md — adding papers to key-papers

`readme.md` is the source of truth. Everything else is derived from it:
the citation map (`assets/`), the quality scores (`filter/`), and the Telegram
badges. Adding a paper means editing one readme bullet and then re-deriving
the rest in the order below. Distilled from a real 7-paper run (Sep 2026),
including the mistakes.

## Quick checklist

```text
0. intake      pick papers with the user; copy identifiers verbatim, never from memory
1. readme      one bullet per paper, right section, newest first, first URL = key
2. filter      collect_readme -> fetch_meta -> extract_fulltext --only-keys ...
   CHECK       fulltext '#' title == readme title for every new key
3. telegram    tg/find.py per paper -> prepend a section to tg_link_choices.md -> wait for picks
4. map         parse_readme -> fetch_refs -> build_graph -> import_litmaps <csv>
5. gpu         rsync inputs -> run queue with --only-keys -> pull scores_*.jsonl + reviews
   local       score_dgcbert.py --device cpu
6. badges      build_report.py -> add_score_badges.py -> read the new lines back
7. finish      report scores, list TG picks pending, do not commit / destroy unless asked
```

## Conventions

- Bullet: `- Title — [url](url) · [url2](url2) [⌲ tg](…) [⚖ +0.29 · 3/7](filter/report.md#anchor)`.
  Links separated by ` · `. Badges are never typed by hand: TG badge only after
  the user's pick, score badge only via `filter/add_score_badges.py`.
- Node key comes from the **first** URL on the bullet (`classify()` in
  `src/common.py`): `arxiv:2410.04444`, `doi:10.1038/s41586-023-06924-6`,
  `openreview:pOoKI3ouv1`, `acl:2022.acl-long.360`, `url:<slug>`.
  Only `arxiv` / `doi` / `openreview` / `acl` are scoreable.
- Within a section bullets are newest first. Check the neighbours' dates
  (arXiv id = YYMM) before inserting.
- Python: pathlib, single quotes, PEP8, progress output for anything slow.
- Report macro metrics when summarising scores.

## Windows / shell traps (they all happened)

- PowerShell 5 has no `<<'PY'` heredocs and rejects `&&`. Do not paste bash or
  multi-line python into `Shell`. Write a `.py` under `%TEMP%` with the Write
  tool and run it, or write the `.sh` into `filter/remote/` and run it over SSH.
- Non-ASCII output from python dies with `cp1252` — set
  `$env:PYTHONIOENCODING='utf-8'` first.
- Shell scripts for the Linux box must be LF. The Write tool may produce CRLF;
  the first `_score_new7.sh` launch failed on `$'\r'`. Normalise locally
  (`p.write_bytes(p.read_bytes().replace(b'\r\n', b'\n'))`) and/or on the box
  (`sed -i 's/\r$//' script.sh`) before `bash script.sh`.
- rsync: prepend `D:\Programs\msys64\usr\bin` to `PATH`, use
  `-e 'ssh -o StrictHostKeyChecking=accept-new -i /c/Users/Asus/.ssh/id_rsa -p <PORT>'`,
  local paths as `/d/Projects/key-papers/...`, and always
  `--rsync-path=//usr/local/bin/rsync` (`/usr/bin/rsync` on the Vast image is a
  0-byte stub). Plain Windows `ssh -i C:\Users\Asus\.ssh\id_rsa -p <PORT>` is
  fine for running commands.
- Do not grep a file in the same tool batch as the script that rewrites it;
  the result is stale. Read after the write finishes.

## 0. Intake

Source is usually a Litmaps CSV export (`D:\Downloads\untitled (N).csv`).
Columns: identifier, title, authors, venue, year, abstract, …, citation and
reference counts. arXiv rows carry `10.48550/arxiv.XXXX.XXXXX`; journal rows
carry the real DOI only; some rows say `(missing DOI)`.

- Dedupe against the readme by arXiv id, DOI and normalised title. Expect
  duplicates inside the CSV itself.
- Show the user the new papers grouped by suggested section and let them pick.
  Nothing is added without a pick.
- **Copy identifiers verbatim.** If the CSV has only a Nature DOI, the bullet
  gets only that DOI. Never supply an arXiv id from memory: the FunSearch row
  got `arxiv:2308.16117` guessed for it, that id is an Al-Cu alloys paper, and
  all ten models scored the wrong PDF under FunSearch's name. Nothing in the
  pipeline catches this except the title check in step 2.
- If an id really must be found (`(missing DOI)` rows), web-search, open
  `arxiv.org/abs/<id>` and confirm the title before writing it down.

## 1. Edit `readme.md`

One `- Title — [url](url)` bullet per paper in the matching `## Section`,
newest first. Short parentheticals in the title are fine (`(Nature 2023)`).
No badges yet.

## 2. Filter inputs

```powershell
python filter/collect_readme.py                     # filter/papers.jsonl (+ tg_posts from the sqlite index)
python filter/fetch_meta.py                         # filter/meta.jsonl via arXiv API / Crossref / OpenReview
python filter/extract_fulltext.py --only-keys k1,k2 # filter/fulltext/<safe_key>.md, fulltext_index.jsonl, fulltext.zip
```

- `fetch_meta.py` always reports 8 incomplete `openreview:*` keys: OpenReview
  is Cloudflare-blocked from this machine. Ignore.
- `extract_fulltext.py` tries cached HTML → arxiv/ar5iv HTML → the bullet's own
  URLs → local PDF (`filter/fulltext/<safe_key>.pdf`) → remote PDF
  (`arxiv.org/pdf`, `EXTRA_PDF_URLS`). Nature article HTML downloads fine
  (~18k tokens). For blocked pages add an `EXTRA_PDF_URLS` entry or drop a
  PDF next to the markdown. Always pass `--only-keys`; a bare run reprocesses
  all ~330 papers.
- **Mandatory check** for every new key: read the first ~10 lines of
  `filter/fulltext/<safe_key>.md` and grep the key in `filter/meta.jsonl`. Both
  titles must be the readme paper. A mismatch means a wrong identifier — go
  back to step 0, fix the bullet, delete the bad `fulltext/*.md`, redo.
- `safe_key` replaces `:` and `/` with `_`:
  `arxiv_2410.04444.md`, `doi_10.1038_s41586-023-06924-6.md`.

## 3. Telegram candidates

Index: `tg/ml_folder.sqlite` (~410 MB, untracked). Refresh with
`python tg/export.py` (`TG_API_ID`, `TG_API_HASH` in `.env`).

```powershell
python tg/find.py https://arxiv.org/abs/2410.04444 --md    # tg_link_choices.md-style block
python tg/find.py 2410.04444 --badge                       # ready-to-paste badge
```

- `collect_readme.py` already stores up to 20 hits per paper in
  `papers.jsonl[tg_posts]`, and `report.md` lists them — that is the same
  candidate set.
- Prepend a `## New from <source>` section to `tg_link_choices.md` with one
  block per paper. **Never regenerate the whole file with
  `tg/find_missing.py`** — the rest carries manual `[skip]` annotations.
- Triage before proposing: dedicated post about the paper (good);
  `[digest]` — Axis of Ordinary "Links for …", boris_again дайджест (usually
  skip); `j_links` / Just links (skip); silent reposts (skip); `[title match]`
  (read the post). Key hits on older papers are often *citing* posts about
  something else — Linear Attention (2020) matched Mamba-2 and Linformer
  reviews. Read the text when in doubt.
- Wait for the user: `paper: handle/id`, `skip`, or `both: a/1 b/2`. Then
  append to the readme line, after the links and before any score badge:
  `[⌲ tg](https://t-me.translate.goog/s/<handle>/<id>?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)`.
  Re-running `add_score_badges.py` re-orders the score badge to the end.

## 4. Citation map

```powershell
python src/parse_readme.py                          # assets/catalog.json (fetches new arXiv meta into assets/arxiv_meta.json)
python src/fetch_refs.py                            # assets/refs.json, assets/page_meta.json — only new nodes hit the network
python src/build_graph.py                           # assets/graph.json, assets/graph_data.js
python src/import_litmaps.py "D:\Downloads\untitled (3).csv"   # assets/litmaps.json overlay
```

Order matters; each step is well under a minute when cached. Node count must
grow by exactly the number of added bullets, and `fetch_refs` should print
`fetched=<that number>`. Dates come from arXiv meta / Crossref; override in
`assets/known_meta.json` if wrong. `python src/verify_map.py --preview`
(playwright) renders the map and refreshes `assets/preview.png`.

If a key changes (FunSearch went `arxiv:` → `doi:`), stale entries remain in
`arxiv_meta.json` / `refs.json` / `page_meta.json` under the old id. Harmless.

## 5. Scoring on the Vast.ai box

Ask before spending. `vastai show user --raw` → `credit`; RTX PRO 6000 WS is
~$1.25/h. Costs seen: 7 papers ≈ $1.3 (SciJudge pairs dominate), 1 paper ≈ $0.4.

- Instance: `vastai show instance <id> --raw` → `public_ipaddr` and
  `ports["22/tcp"][0].HostPort` for **direct** SSH (`ssh_host`/`ssh_port` is
  the slow proxy). Last known: `50549154`, label `key-papers-filter`,
  `66.187.29.137:28448`, user `root`. Layout: data `/workspace/filter`,
  scripts `/workspace/filter/remote`, venv `/venv/main`, HF cache
  `/workspace/.hf_home`; models already downloaded (~336 GB used). A fresh box
  needs `filter/remote/setup.sh` (see the pinned vLLM / torch stack in it).
- Upload only the delta: `papers.jsonl`, `meta.jsonl`, `fulltext_index.jsonl`,
  the new `fulltext/*.md`, and the run script. rsync into `/tmp/xfer/` then
  `cp -f` into place (or rsync straight into `/workspace/filter/`). Do not
  ship `fulltext.zip` for a handful of papers.
- Run script: copy `filter/remote/_score_new7.sh`, change `KEYS` and the log
  name, LF endings. Queue: `naip --model both` → `scijudge` →
  `openreviewer-8b` → `sea-e` → `cyclereviewer-8b` → `deepreviewer-7b-fast` →
  `deepreviewer-14b` → `deepreviewer-7b`; DeepReviewer models take
  `--max-paper-chars 48000`; reviewers take `--only-keys "$KEYS"`. Launch
  with `nohup bash … > logs/<name>.nohup 2>&1 &`, poll with
  `grep -E '\[step\]|cached,|FAILED' logs/<name>.log`.
- Every scorer is incremental (`scored_keys()` skips cached keys), so running
  the whole queue for one new key is safe. To rescore a key, drop its rows and
  review file first (pattern in `filter/remote/_rescore_eight.sh`).
- Timings for one paper: NAIP < 1 min; SciJudge ~1 min load + ~1.5 min for
  ~60 new pairs; each reviewer 1–4 min including vLLM boot; DR-7B Standard is
  the slowest. Seven papers took ~50 min wall, ~40 of them SciJudge.
- SciJudge rebuilds Bradley-Terry per publication year, so every run shifts
  `scijudge_bt` and the final score of the *existing* papers slightly.
  Expected; `add_score_badges.py` then touches ~90 readme lines.
- DGC-BERT is local: `python filter/score_dgcbert.py --device cpu` (~1 min,
  incremental).
- Pull back the nine `scores_*.jsonl` (naipv1, naipv2, scijudge,
  openreviewer-8b, sea-e, cyclereviewer-8b, deepreviewer-7b-fast,
  deepreviewer-14b, deepreviewer-7b) and `reviews/<model>/<safe_key>.md` for
  the new keys. Confirm each new key is in all ten score files with no
  `error` / `unparsed` rows. `scores_deepreviewer-7b.jsonl` legitimately has
  extra retry rows; the aggregator keeps the last valid row per key — do not
  dedupe by hand.
- Leave the instance running unless told otherwise; report credit and rate.
  Destroy only on request: `vastai destroy instance <id> -y`.

## 6. Aggregate and badges

```powershell
python filter/build_report.py        # filter/scores.csv + filter/report.md
python filter/add_score_badges.py    # rewrites every [⚖ …] badge in readme.md; idempotent
```

- Badge: `[⚖ +0.54 · 6/7](filter/report.md#doi-10.1038-s41586-023-06924-6)`,
  `· WATCH` / `· DROP` appended when the verdict is not KEEP. Anchor =
  key with `:` and `/` → `-`.
- Read the new readme lines back with the Read tool and check the
  `scores.csv` row title equals the readme title. This is where the FunSearch
  mismatch surfaced (`Strengthening from dislocation restructuring…` under an
  Agents key with a DROP badge).
- `pytest filter/test_aggregate.py` if `filter/aggregate.py` was touched.

## 7. Finish

- Report per paper: final score, accept votes, verdict, notable model
  disagreements; list the TG picks still pending with the recommended post.
- Do not commit unless asked. `filter/remote/_*.sh` are one-off helpers and
  stay untracked. Delete temp scripts and any fulltext for a discarded key.

## Pipeline reference

| Stage | Command | Output |
|---|---|---|
| catalog | `src/parse_readme.py` | `assets/catalog.json`, `assets/arxiv_meta.json` |
| refs | `src/fetch_refs.py` | `assets/refs.json`, `assets/page_meta.json` |
| graph | `src/build_graph.py` | `assets/graph.json`, `assets/graph_data.js` |
| overlay | `src/import_litmaps.py <csv>` | `assets/litmaps.json` |
| papers | `filter/collect_readme.py` | `filter/papers.jsonl` |
| meta | `filter/fetch_meta.py` | `filter/meta.jsonl` |
| fulltext | `filter/extract_fulltext.py --only-keys` | `filter/fulltext/`, `fulltext_index.jsonl`, `fulltext.zip` |
| abstract scorers (GPU) | `filter/remote/score_naip.py`, `score_scijudge.py` | `scores_naipv1/naipv2/scijudge.jsonl` |
| full-paper reviewers (GPU) | `filter/remote/score_reviewers.py --model … --only-keys …` | `scores_<model>.jsonl`, `reviews/<model>/` |
| abstract scorer (CPU) | `filter/score_dgcbert.py --device cpu` | `scores_dgcbert.jsonl` |
| aggregate | `filter/build_report.py` | `filter/scores.csv`, `filter/report.md` |
| badges | `filter/add_score_badges.py` | `readme.md` |
| telegram | `tg/export.py`, `tg/find.py`, `tg/find_missing.py` (full regen only) | `tg/ml_folder.sqlite`, `tg_link_choices.md` |

Design notes for each stage live in `.cursor/plans/*.plan.md`.
