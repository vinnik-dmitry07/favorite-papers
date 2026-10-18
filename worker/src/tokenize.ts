import embedJson from '../embed.json'

export interface EmbedConfig {
  schema_version: number
  reader_schema: number
  model: string
  dimensions: number
  metric: string
  pooling: string
  max_input_tokens: number
  query_template: string
  passage_template: string
  clean_version: number
  chunk_version: number
  max_code_points: number
  overlap_code_points: number
  tokenizer: {
    id: string
    revision: string
    do_lower_case: boolean
    strip_accents: boolean
    tokenize_chinese_chars: boolean
    max_input_chars_per_word: number
    cls_token: string
    sep_token: string
    unk_token: string
    vocab_file: string
    vocab_sha256: string
  }
  limits: {
    authors: number
    citation_default: number
    citation_max: number
    traverse_hops_default: number
    traverse_hops_max: number
    traverse_nodes_max: number
    content_code_points: number
    search_k_default: number
    search_k_max: number
    snippet_code_points: number
    id_bytes_max: number
    query_code_points_max: number
    response_bytes_max: number
    summary_title_code_points: number
    pointer_ttl_seconds: number
    deadline_seconds: number
    grace_seconds: number
    paper_cache_entries: number
    paper_cache_bytes: number
    search_cache_entries: number
  }
  search_enabled: boolean
  rate_limit: { namespace_id: string, limit: number, period_seconds: number }
  vectorize: { index_name: string, free_dimensions: number, probe_vectors: number }
  worker_name: string
  r2_bucket: string
}

export const embed = embedJson as EmbedConfig

export function pointLength(text: string): number {
  let count = 0
  for (let index = 0; index < text.length; index = nextPoint(text, index)) {
    count += 1
  }
  return count
}

function nextPoint(text: string, index: number): number {
  const point = text.codePointAt(index) ?? 0
  return index + (point > 0xffff ? 2 : 1)
}

export function slicePoints(text: string, start: number, end?: number): string {
  const stop = end ?? Number.MAX_SAFE_INTEGER
  let count = 0
  let from = text.length
  let to = text.length
  for (let index = 0; index < text.length; index = nextPoint(text, index)) {
    if (count === start) {
      from = index
    }
    if (count === stop) {
      to = index
      return text.slice(from, to)
    }
    count += 1
  }
  return text.slice(from, to)
}

function isPunctuation(char: string): boolean {
  const cp = char.codePointAt(0) ?? 0
  if (
    (cp >= 33 && cp <= 47)
    || (cp >= 58 && cp <= 64)
    || (cp >= 91 && cp <= 96)
    || (cp >= 123 && cp <= 126)
  ) {
    return true
  }
  return /^\p{P}$/u.test(char)
}

function isWhitespace(char: string): boolean {
  if (char === ' ' || char === '\t' || char === '\n' || char === '\r') {
    return true
  }
  return /^\p{Zs}$/u.test(char)
}

function isControl(char: string): boolean {
  if (char === '\t' || char === '\n' || char === '\r') {
    return false
  }
  return /^\p{C}$/u.test(char)
}

function isChinese(cp: number): boolean {
  return (
    (cp >= 0x4e00 && cp <= 0x9fff)
    || (cp >= 0x3400 && cp <= 0x4dbf)
    || (cp >= 0x20000 && cp <= 0x2a6df)
    || (cp >= 0x2a700 && cp <= 0x2b73f)
    || (cp >= 0x2b740 && cp <= 0x2b81f)
    || (cp >= 0x2b820 && cp <= 0x2ceaf)
    || (cp >= 0xf900 && cp <= 0xfaff)
    || (cp >= 0x2f800 && cp <= 0x2fa1f)
  )
}

export class WordPieceTokenizer {
  private readonly ids = new Map<string, number>()
  private readonly unkId: number
  private readonly clsId: number
  private readonly sepId: number

  constructor(vocabText: string) {
    const lines = vocabText.split(/\r?\n/)
    if (lines.length > 0 && lines[lines.length - 1] === '') {
      lines.pop()
    }
    lines.forEach((line, index) => {
      this.ids.set(line, index)
    })
    const tok = embed.tokenizer
    const unk = this.ids.get(tok.unk_token)
    const cls = this.ids.get(tok.cls_token)
    const sep = this.ids.get(tok.sep_token)
    if (unk === undefined || cls === undefined || sep === undefined) {
      throw new Error('vocab is missing a special token')
    }
    this.unkId = unk
    this.clsId = cls
    this.sepId = sep
  }

  tokenIds(template: string, text: string): number[] {
    const pieces = this.basic(template ? template + text : text)
    const ids = [this.clsId]
    for (const piece of pieces) {
      ids.push(...this.wordpiece(piece))
    }
    ids.push(this.sepId)
    return ids
  }

  private basic(text: string): string[] {
    let flattened = ''
    for (const char of text) {
      const cp = char.codePointAt(0) ?? 0
      if (cp === 0 || cp === 0xfffd || isControl(char)) {
        continue
      }
      flattened += isWhitespace(char) ? ' ' : char
    }
    if (embed.tokenizer.tokenize_chinese_chars) {
      let spaced = ''
      for (const char of flattened) {
        const cp = char.codePointAt(0) ?? 0
        if (isChinese(cp)) {
          spaced += ` ${char} `
        } else {
          spaced += char
        }
      }
      flattened = spaced
    }
    const output: string[] = []
    for (const raw of flattened.split(/\s+/)) {
      if (!raw) {
        continue
      }
      let token = raw
      if (embed.tokenizer.do_lower_case) {
        token = token.toLowerCase()
      }
      if (embed.tokenizer.strip_accents) {
        token = token.normalize('NFD').replace(/\p{Mn}/gu, '')
      }
      output.push(...this.splitPunctuation(token))
    }
    return output
  }

  private splitPunctuation(token: string): string[] {
    const parts: string[] = []
    let chars = ''
    for (const char of token) {
      if (isPunctuation(char)) {
        if (chars) {
          parts.push(chars)
          chars = ''
        }
        parts.push(char)
      } else {
        chars += char
      }
    }
    if (chars) {
      parts.push(chars)
    }
    return parts
  }

  private wordpiece(token: string): number[] {
    const chars = Array.from(token)
    if (chars.length > embed.tokenizer.max_input_chars_per_word) {
      return [this.unkId]
    }
    const whole = this.ids.get(token)
    if (whole !== undefined) {
      return [whole]
    }
    const ids: number[] = []
    let start = 0
    while (start < chars.length) {
      let end = chars.length
      let found: number | undefined
      while (start < end) {
        let piece = chars.slice(start, end).join('')
        if (start > 0) {
          piece = `##${piece}`
        }
        found = this.ids.get(piece)
        if (found !== undefined) {
          break
        }
        end -= 1
      }
      if (found === undefined) {
        return [this.unkId]
      }
      ids.push(found)
      start = end
    }
    return ids
  }
}
