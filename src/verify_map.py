'''Drive src/index.html in Chrome and report what actually rendered.

Run:  python src/verify_map.py [--preview]

Serves the repo root over HTTP so Chrome can load ../assets/.
--preview also refreshes assets/preview.png, the still used in readme.md.
'''

import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from playwright.sync_api import sync_playwright

from common import ASSETS, ROOT

SHOTS = ROOT / 'shots'
PREVIEW = ASSETS / 'preview.png'


class _RootHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, format, *args):
        return


def start_server() -> ThreadingHTTPServer:
    server = ThreadingHTTPServer(('127.0.0.1', 0), _RootHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def map_url(server: ThreadingHTTPServer) -> str:
    return f'http://127.0.0.1:{server.server_address[1]}/src/index.html'


def preview() -> None:
    '''Render the still that readme.md links to.'''
    server = start_server()
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='chrome')
        page = browser.new_page(viewport={'width': 1600, 'height': 900},
                                device_scale_factor=1.5)
        page.goto(map_url(server), wait_until='load')
        page.wait_for_timeout(1500)
        page.screenshot(path=str(PREVIEW))
        browser.close()
    server.shutdown()
    print(f'wrote {PREVIEW}')


def main() -> None:
    SHOTS.mkdir(parents=True, exist_ok=True)
    server = start_server()
    target = map_url(server)
    errors: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='chrome')
        page = browser.new_page(viewport={'width': 1440, 'height': 860})
        page.on('console', lambda m: errors.append(f'console.{m.type}: {m.text}')
                if m.type in ('error', 'warning') else None)
        page.on('pageerror', lambda e: errors.append(f'pageerror: {e}'))
        page.goto(target, wait_until='load')
        page.wait_for_timeout(1200)

        counts = page.evaluate('''() => {
            const shown = [...document.querySelectorAll('.labels text')]
                .filter(t => t.getAttribute('display') !== 'none');
            const topCites = Math.max(...[...document.querySelectorAll(
                '.nodes circle')].map(c => +c.getAttribute('r')));
            return {
                nodes: document.querySelectorAll('.nodes g').length,
                circles: document.querySelectorAll('.nodes circle').length,
                edges: document.querySelectorAll('.edges path').length,
                labelsShown: shown.length,
                topNodeLabelled: shown.some(t => t.textContent.includes('GRPO')),
                biggestRadius: topCites,
                axisTicks: document.querySelectorAll('.axis .tick').length,
                stats: document.getElementById('stats').textContent,
                fills: new Set([...document.querySelectorAll('.nodes circle')]
                    .map(c => c.getAttribute('fill'))).size,
                legendChips: document.querySelectorAll('#legend span').length,
            };
        }''')
        print('render:', counts)
        if counts.get('fills', 0) < 5:
            errors.append('nodes are not colored by tag')
        if counts.get('legendChips', 0) < 10:
            errors.append('tag legend missing')
        page.screenshot(path=str(SHOTS / '01-overview.png'))

        # Hover the most-cited node and confirm the tooltip and highlighting.
        target = page.evaluate('''() => {
            const els = [...document.querySelectorAll('.nodes circle')];
            let best = null, bestR = -1;
            els.forEach((c, i) => {
                const r = +c.getAttribute('r');
                if (r > bestR) { bestR = r; best = i; }
            });
            const box = els[best].getBoundingClientRect();
            return {i: best, x: box.x + box.width / 2, y: box.y + box.height / 2};
        }''')
        page.mouse.move(target['x'], target['y'])
        page.wait_for_timeout(500)
        hover = page.evaluate('''() => ({
            tipOpacity: getComputedStyle(document.getElementById('tip')).opacity,
            tipText: document.getElementById('tip').innerText.replace(/\\n/g, ' | '),
            dimmed: document.querySelectorAll('.nodes g.dim').length,
            litEdges: [...document.querySelectorAll('.edges path')]
                .filter(p => +p.getAttribute('stroke-opacity') > 0.5).length,
        })''')
        print('hover:', hover)
        if 'Litmaps' not in hover.get('tipText', ''):
            errors.append('tooltip missing Litmaps citation counts')
        page.screenshot(path=str(SHOTS / '02-hover.png'))

        page.mouse.click(target['x'], target['y'])
        page.wait_for_timeout(300)
        page.mouse.move(20, 400)
        page.wait_for_timeout(400)
        held = page.evaluate('''() => ({
            tipOpacity: getComputedStyle(document.getElementById('tip')).opacity,
            tipText: document.getElementById('tip').innerText,
            dimmed: document.querySelectorAll('.nodes g.dim').length,
            held: document.querySelectorAll('.nodes g.held').length,
            litEdges: [...document.querySelectorAll('.edges path')]
                .filter(p => +p.getAttribute('stroke-opacity') > 0.5).length,
        })''')
        print('held after click+leave:', held)

        page.evaluate('''() => { window.__opened = [];
            window.open = (url) => { window.__opened.push(url); }; }''')
        page.mouse.dblclick(target['x'], target['y'])
        page.wait_for_timeout(300)
        print('dblclick opened:', page.evaluate('() => window.__opened'))

        page.keyboard.press('Escape')
        page.wait_for_timeout(300)
        print('after Esc:', page.evaluate('''() => ({
            held: document.querySelectorAll('.nodes g.held').length,
            dimmed: document.querySelectorAll('.nodes g.dim').length,
            tipOpacity: getComputedStyle(document.getElementById('tip')).opacity,
        })'''))

        # Zooming while a paper is hovered must keep its links highlighted.
        page.mouse.move(target['x'], target['y'])
        page.wait_for_timeout(300)
        page.mouse.wheel(0, -240)
        page.wait_for_timeout(400)
        print('hover kept during zoom:', page.evaluate(
            '''() => [...document.querySelectorAll('.edges path')]
                   .filter(p => +p.getAttribute('stroke-opacity') > 0.5).length'''))
        page.click('#reset')
        page.wait_for_timeout(500)
        page.mouse.move(4, 400)
        page.wait_for_timeout(300)

        page.fill('#search', 'grpo')
        page.wait_for_timeout(500)
        search = page.evaluate('''() => ({
            dimmed: document.querySelectorAll('.nodes g.dim').length,
            note: document.getElementById('note').textContent.slice(0, 44),
            labelsShown: [...document.querySelectorAll('.labels text')]
                .filter(t => t.getAttribute('display') !== 'none').length,
        })''')
        print('search grpo:', search)
        page.screenshot(path=str(SHOTS / '03-search.png'))
        page.fill('#search', '')
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)

        page.evaluate('''() => {
            const chip = [...document.querySelectorAll('#legend span')]
                .find(s => s.dataset.topic === 'RL');
            if (chip) chip.click();
        }''')
        page.wait_for_timeout(400)
        tag_filter = page.evaluate('''() => ({
            dimmed: document.querySelectorAll('.nodes g.dim').length,
            note: document.getElementById('note').textContent.slice(0, 28),
            on: [...document.querySelectorAll('#legend span.on')]
                .map(s => s.dataset.topic),
        })''')
        print('tag RL:', tag_filter)
        if tag_filter['dimmed'] < 200:
            errors.append('tag filter did not dim other topics')
        page.evaluate('''() => {
            const chip = [...document.querySelectorAll('#legend span')]
                .find(s => s.dataset.topic === '');
            if (chip) chip.click();
        }''')
        page.wait_for_timeout(300)

        page.check('#citefilter')
        page.wait_for_timeout(400)
        cite_filter = page.evaluate('''() => {
            const seeds = [
                'arxiv:2407.21783', 'arxiv:2501.00656', 'arxiv:2506.10947',
                'arxiv:2601.11061', 'arxiv:2604.01754',
            ];
            const gs = [...document.querySelectorAll('.nodes g')];
            const brightIds = gs
                .map((g, i) => g.classList.contains('dim')
                    ? null : window.GRAPH_DATA.nodes[i].id)
                .filter(Boolean);
            return {
                dimmed: gs.filter(g => g.classList.contains('dim')).length,
                bright: brightIds.length,
                note: document.getElementById('note').textContent.slice(0, 36),
                missingSeeds: seeds.filter(id => brightIds.indexOf(id) < 0),
            };
        }''')
        print('cite filter:', cite_filter)
        if cite_filter['bright'] < 5 or cite_filter['bright'] > 80:
            errors.append(
                f'cite filter kept {cite_filter["bright"]} papers, expected a seed neighbourhood'
            )
        if cite_filter['dimmed'] < 200:
            errors.append('cite filter did not dim papers that do not cite the seeds')
        if cite_filter['missingSeeds']:
            errors.append('cite filter hid seeds ' + ', '.join(cite_filter['missingSeeds']))
        page.screenshot(path=str(SHOTS / '06-cite-filter.png'))
        page.uncheck('#citefilter')
        page.wait_for_timeout(300)

        page.check('#tgfilter')
        page.wait_for_timeout(400)
        tg_filter = page.evaluate('''() => {
            const nodes = window.GRAPH_DATA.nodes;
            const withTg = nodes.filter(n => n.telegram).length;
            const gs = [...document.querySelectorAll('.nodes g')];
            const bright = gs.filter(g => !g.classList.contains('dim')).length;
            return {
                withTg,
                bright,
                dimmed: gs.filter(g => g.classList.contains('dim')).length,
                note: document.getElementById('note').textContent.slice(0, 36),
            };
        }''')
        print('telegram filter:', tg_filter)
        if tg_filter['withTg'] < 50:
            errors.append('too few catalog nodes marked telegram')
        if tg_filter['bright'] != tg_filter['withTg']:
            errors.append(
                f'telegram filter kept {tg_filter["bright"]}, '
                f'expected {tg_filter["withTg"]}'
            )
        if tg_filter['dimmed'] < 50:
            errors.append('telegram filter did not dim papers without a badge')
        page.screenshot(path=str(SHOTS / '07-telegram-filter.png'))
        page.uncheck('#tgfilter')
        page.wait_for_timeout(300)

        page.select_option('#labels', 'all')
        page.wait_for_timeout(500)
        print('labels=all:', page.evaluate(
            '''() => [...document.querySelectorAll('.labels text')]
                   .filter(t => t.getAttribute('display') !== 'none').length'''))
        page.select_option('#labels', 'key')
        page.uncheck('#edges')
        page.wait_for_timeout(300)
        print('edges hidden:', page.evaluate(
            '''() => document.querySelector('.edges').getAttribute('display')'''))
        page.check('#edges')

        if not page.evaluate(
            '''() => document.getElementById('addcited-wrap').hidden'''
        ):
            errors.append('+ cited should be hidden on cited-by axis')
        cited_axis = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
            };
        }''')
        page.select_option('#yaxis', 'cites')
        page.wait_for_timeout(900)
        cites_axis = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
                biggestRadius: Math.max(...[...document.querySelectorAll(
                    '.nodes circle')].map(c => +c.getAttribute('r'))),
            };
        }''')
        moved = sum(1 for a, b in zip(cited_axis['ys'], cites_axis['ys'])
                    if abs(a - b) > 8)
        print('yaxis cited:', cited_axis['captions'], cited_axis['note'][:72])
        print('yaxis cites:', cites_axis['captions'], cites_axis['note'][:72],
              'moved', moved, 'r', cites_axis['biggestRadius'])
        if not any('cited by more' in c for c in cited_axis['captions']):
            errors.append('cited-by axis caption missing')
        if not any('cites more' in c for c in cites_axis['captions']):
            errors.append('cites axis caption missing')
        if 'cited by other' not in cited_axis['note']:
            errors.append('cited-by footer missing')
        if 'outgoing cites' not in cites_axis['note']:
            errors.append('cites footer missing')
        if moved < 20:
            errors.append(f'y-axis mode barely moved nodes ({moved})')
        page.select_option('#yaxis', 'parents')
        page.wait_for_timeout(900)
        parents_axis = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
            };
        }''')
        moved_par = sum(1 for a, b in zip(cites_axis['ys'], parents_axis['ys'])
                        if abs(a - b) > 8)
        print('yaxis parents: moved vs cites', moved_par)
        if not any('parent papers' in c for c in parents_axis['captions']):
            errors.append('parent-cites axis caption missing')
        if 'parent cites' not in parents_axis['note']:
            errors.append('parent-cites footer missing')
        if moved_par < 10:
            errors.append(
                f'parent-cites y-axis barely moved vs cites ({moved_par})'
            )
        page.select_option('#yaxis', 'children')
        page.wait_for_timeout(900)
        children_axis = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
            };
        }''')
        moved_ch = sum(1 for a, b in zip(cites_axis['ys'], children_axis['ys'])
                       if abs(a - b) > 8)
        print('yaxis children: moved vs cites', moved_ch)
        if not any('nested outgoing' in c for c in children_axis['captions']):
            errors.append('nested-cites axis caption missing')
        if 'nested outgoing' not in children_axis['note']:
            errors.append('nested-cites footer missing')
        if moved_ch < 10:
            errors.append(
                f'child-rollup y-axis barely moved vs cites ({moved_ch})'
            )
        page.select_option('#yaxis', 'bonus')
        page.wait_for_timeout(900)
        bonus_axis = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
            };
        }''')
        moved_bo = sum(1 for a, b in zip(cites_axis['ys'], bonus_axis['ys'])
                       if abs(a - b) > 8)
        print('yaxis bonus: moved vs cites', moved_bo)
        if not any('less-cited targets' in c for c in bonus_axis['captions']):
            errors.append('bonus-cites axis caption missing')
        if '1/cited' not in bonus_axis['note']:
            errors.append('bonus-cites footer missing')
        if moved_bo < 5:
            errors.append(
                f'bonus-cites y-axis barely moved vs cites ({moved_bo})'
            )
        if page.evaluate(
            '''() => document.getElementById('addcited-wrap').hidden'''
        ):
            errors.append('+ cited should be shown on bonus axis')
        page.select_option('#yaxis', 'cites')
        page.wait_for_timeout(200)
        if page.evaluate(
            '''() => document.getElementById('addcited-wrap').hidden'''
        ):
            errors.append('+ cited should be shown on cites axis')
        page.check('#addcited')
        page.wait_for_timeout(900)
        both_axis = page.evaluate('''() => ({
            captions: [...document.querySelectorAll('.caption')]
                .map(t => t.textContent),
            note: document.getElementById('note').textContent,
            ys: [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            }),
        })''')
        print('yaxis cites + cited:', both_axis['captions'], both_axis['note'][:80])
        if not any('cited-by + cites' in c for c in both_axis['captions']):
            errors.append('cited+cites axis caption missing')
        if 'cited by plus outgoing' not in both_axis['note']:
            errors.append('cited+cites footer missing')
        moved_add = sum(
            1 for a, b in zip(cites_axis['ys'], both_axis['ys'])
            if abs(a - b) > 8
        )
        print('yaxis cites + cited: moved vs cites', moved_add)
        if moved_add < 20:
            errors.append(
                f'+ cited barely moved nodes vs cites-only ({moved_add})'
            )
        page.select_option('#yaxis', 'parents')
        page.wait_for_timeout(900)
        cited_par = page.evaluate('''() => ({
            captions: [...document.querySelectorAll('.caption')]
                .map(t => t.textContent),
            note: document.getElementById('note').textContent,
        })''')
        print('yaxis parents + cited:', cited_par['captions'],
              cited_par['note'][:80])
        if not any('cited-by + parent cites' in c for c in cited_par['captions']):
            errors.append('cited+parents axis caption missing')
        if 'cited by plus outgoing parent' not in cited_par['note']:
            errors.append('cited+parents footer missing')
        page.uncheck('#addcited')
        page.select_option('#yaxis', 'citations')
        page.wait_for_timeout(900)
        if not page.evaluate(
            '''() => document.getElementById('addcited-wrap').hidden'''
        ):
            errors.append('+ cited should be hidden on citation-count axis')
        cites_num = page.evaluate('''() => {
            const captions = [...document.querySelectorAll('.caption')]
                .map(t => t.textContent);
            const ys = [...document.querySelectorAll('.nodes g')].map(g => {
                const m = /translate\\(([^,]+),([^)]+)\\)/.exec(
                    g.getAttribute('transform'));
                return +m[2];
            });
            const ticks = [...document.querySelectorAll('.axis .tick text')]
                .map(t => t.textContent);
            return {
                captions,
                note: document.getElementById('note').textContent,
                ys,
                ticks,
                biggestRadius: Math.max(...[...document.querySelectorAll(
                    '.nodes circle')].map(c => +c.getAttribute('r'))),
            };
        }''')
        moved_cit = sum(1 for a, b in zip(cited_axis['ys'], cites_num['ys'])
                        if abs(a - b) > 8)
        print('yaxis citations: ticks', cites_num['ticks'],
              'moved', moved_cit, 'r', cites_num['biggestRadius'])
        if not any('more citations' in c for c in cites_num['captions']):
            errors.append('citation-count axis caption missing')
        if 'Litmaps citation count' not in cites_num['note']:
            errors.append('citation-count footer missing')
        if moved_cit < 20:
            errors.append(
                f'citation-count y-axis barely moved nodes ({moved_cit})'
            )
        if not any(t in cites_num['ticks'] for t in ('1k', '2k', '5k', '10k', '20k')):
            errors.append('citation-count axis missing thousands ticks')
        page.select_option('#yaxis', 'cited')
        page.wait_for_timeout(600)

        # Zoom in on the dense recent cluster.
        page.mouse.move(1050, 470)
        for _ in range(3):
            page.mouse.wheel(0, -260)
            page.wait_for_timeout(150)
        page.wait_for_timeout(700)
        zoomed = page.evaluate('''() => {
            const shown = [...document.querySelectorAll('.labels text')]
                .filter(e => e.getAttribute('display') !== 'none');
            return {
                transform: document.querySelectorAll('svg > g')[1]
                    .getAttribute('transform'),
                labelsShown: shown.length,
                renderedFontPx: shown[0].getBoundingClientRect().height,
                renderedRadiusPx:
                    document.querySelector('.nodes circle')
                        .getBoundingClientRect().width,
            };
        }''')
        print('zoomed:', zoomed)
        page.screenshot(path=str(SHOTS / '04-zoom.png'))

        page.click('#reset')
        page.wait_for_timeout(600)
        print('after reset:', page.evaluate(
            '''() => document.querySelectorAll('svg > g')[1].getAttribute('transform')'''))

        # Narrow viewport re-layout.
        page.set_viewport_size({'width': 900, 'height': 640})
        page.wait_for_timeout(900)
        print('narrow:', page.evaluate('''() => ({
            nodes: document.querySelectorAll('.nodes circle').length,
            offscreen: [...document.querySelectorAll('.nodes circle')]
                .filter(c => {
                    const b = c.getBoundingClientRect();
                    return b.x < -30 || b.y < -30 || b.x > innerWidth + 30
                        || b.y > innerHeight + 30;
                }).length,
        })'''))
        page.screenshot(path=str(SHOTS / '05-narrow.png'))
        browser.close()
    server.shutdown()

    if errors:
        print('\nBROWSER PROBLEMS:')
        for line in errors[:25]:
            print(' ', line)
        sys.exit(1)
    print('\nno console errors')


if __name__ == '__main__':
    main()
    if '--preview' in sys.argv:
        preview()
