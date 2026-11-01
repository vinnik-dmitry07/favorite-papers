/** Shared catalog ranking for production and the runtime probe. */
interface CatalogNode {
  id: string
  title: string
  url?: string | null
  section?: string | null
  topic?: string | null
}

const normalizedNodes = new WeakMap<CatalogNode, { raw: string[], text: string[] }>()

function normalize(value: string): string {
  return value.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
}

export function rankedCatalog<T extends CatalogNode>(nodes: Record<string, T>, query: string, section?: string) {
  const q = normalize(query)
  const terms = q.split(/\s+/)
  return Object.values(nodes).filter((node) => !section || node.section === section).map((node) => {
    const raw = [node.title, node.id, node.url ?? '', node.section ?? '', node.topic ?? '']
    let cached = normalizedNodes.get(node)
    if (!cached || cached.raw.some((value, i) => value !== raw[i])) {
      cached = { raw, text: raw.map(normalize) }
      normalizedNodes.set(node, cached)
    }
    const [title, id, url, sectionText, topic] = cached.text
    let score = 0
    if (!q) score = 1
    else if ([title, id, url].includes(q)) score = 100
    else if (title.includes(q)) score = 50
    else if (id.includes(q) || url.includes(q)) score = 40
    else {
      const haystack = `${title} ${sectionText} ${topic}`
      if (terms.every((term) => haystack.includes(term))) score = 10
    }
    return { node, score }
  }).filter((item) => item.score > 0)
    .sort((a, b) => b.score - a.score || a.node.id.localeCompare(b.node.id))
}
