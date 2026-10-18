import { embed } from './tokenize'

export function canonicalJson(value: unknown): string {
  return JSON.stringify(sortValue(value))
}

function sortValue(value: unknown): unknown {
  if (Array.isArray(value)) {
    return value.map(sortValue)
  }
  if (value && typeof value === 'object') {
    const source = value as Record<string, unknown>
    const sorted: Record<string, unknown> = {}
    for (const key of Object.keys(source).sort()) {
      sorted[key] = sortValue(source[key])
    }
    return sorted
  }
  return value
}

export async function sha256Hex(text: string): Promise<string> {
  const digest = await crypto.subtle.digest(
    'SHA-256',
    new TextEncoder().encode(text),
  )
  return [...new Uint8Array(digest)]
    .map((byte) => byte.toString(16).padStart(2, '0'))
    .join('')
}

export async function signatures(): Promise<{ build: string, embedding: string }> {
  const tok = embed.tokenizer
  const build = await sha256Hex(canonicalJson({
    schema_version: embed.schema_version,
    clean_version: embed.clean_version,
    chunk_version: embed.chunk_version,
    max_code_points: embed.max_code_points,
    overlap_code_points: embed.overlap_code_points,
    max_input_tokens: embed.max_input_tokens,
    passage_template: embed.passage_template,
    tokenizer_id: tok.id,
    tokenizer_revision: tok.revision,
    vocab_sha256: tok.vocab_sha256,
    do_lower_case: tok.do_lower_case,
    strip_accents: tok.strip_accents,
    tokenize_chinese_chars: tok.tokenize_chinese_chars,
    max_input_chars_per_word: tok.max_input_chars_per_word,
    cls_token: tok.cls_token,
    sep_token: tok.sep_token,
    unk_token: tok.unk_token,
  }))
  const embedding = await sha256Hex(canonicalJson({
    model: embed.model,
    dimensions: embed.dimensions,
    metric: embed.metric,
    pooling: embed.pooling,
    query_template: embed.query_template,
    passage_template: embed.passage_template,
    max_input_tokens: embed.max_input_tokens,
    tokenizer_revision: tok.revision,
    vocab_sha256: tok.vocab_sha256,
  }))
  return { build, embedding }
}

export async function vectorIdOf(
  slot: string,
  paperId: string,
  chunkIndex: number,
): Promise<string> {
  return sha256Hex(canonicalJson([slot, paperId, chunkIndex]))
}
