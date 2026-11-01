import { expect, it } from 'vitest'
import { rankedCatalog } from './catalog-search'

it('preserves exact, partial and all-term catalog matching, including mutable input objects', () => {
  const nodes = {
    a: { id: 'arxiv:1', title: 'Ｃafé — Group Policy', url: 'https://arxiv.org/abs/1', section: 'Math', topic: 'RL' },
    b: { id: 'arxiv:2', title: 'Other Policy', section: 'Math' },
  }
  const normalize = (s: string) => s.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
  function reference(query: string, section?: string) {
    const q = normalize(query)
    return Object.values(nodes).filter((node) => !section || node.section === section).map((node) => {
      const title = normalize(node.title), id = normalize(node.id)
      const url = normalize('url' in node ? node.url : '')
      const hay = title + ' ' + normalize(node.section) + ' ' + normalize('topic' in node ? node.topic : '')
      const score = !q ? 1 : [title, id, url].includes(q) ? 100 : title.includes(q) ? 50
        : id.includes(q) || url.includes(q) ? 40 : q.split(/\s+/).every((term) => hay.includes(term)) ? 10 : 0
      return { node, score }
    }).filter((r) => r.score).sort((a, b) => b.score - a.score || a.node.id.localeCompare(b.node.id))
  }
  for (const q of ['', 'café group policy', 'arxiv:1', 'https://arxiv.org/abs/1', 'group Math RL', 'policy', 'q '.repeat(500)]) {
    expect(rankedCatalog(nodes, q)).toEqual(reference(q))
    expect(rankedCatalog(nodes, q, 'Math')).toEqual(reference(q, 'Math'))
  }
  nodes.a.title = 'Changed'
  expect(rankedCatalog(nodes, 'Changed')[0].score).toBe(100)
  expect(rankedCatalog(nodes, 'café')).toHaveLength(0)
})
