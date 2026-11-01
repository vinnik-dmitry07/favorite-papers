/** Stream Python/HF oracle IDs through the actual Worker tokenizer, no model.
 * Bundle with esbuild --bundle --platform=node --format=esm, then run with one
 * JSONL input path. Each row is {id, template, text, ids}; stdout is a report.
 */
import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { createReadStream, readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { WordPieceTokenizer, embed } from '../src/tokenize'

const [input, vocab] = process.argv.slice(2)
assert(input && vocab, 'Usage: tokenizer-parity.mjs INPUT.jsonl VOCAB.txt')
const vocabBytes = readFileSync(resolve(vocab))
const vocabSha = createHash('sha256').update(vocabBytes).digest('hex')
assert.equal(vocabSha, embed.tokenizer.vocab_sha256, 'Tokenizer vocabulary checksum mismatch')
const tokenizer = new WordPieceTokenizer(vocabBytes.toString('utf8'))
const rawHash = createHash('sha256')
const inputStream = createReadStream(resolve(input))
const tokenHash = createHash('sha256')
let checked = 0, mismatchCount = 0
const mismatches: Record<string, unknown>[] = []
function checkLine(line: string) {
  assert(line.trim(), 'Empty tokenizer input row')
  const row = JSON.parse(line)
  assert(typeof row.id === 'string' && typeof row.template === 'string' && typeof row.text === 'string'
    && Array.isArray(row.ids) && row.ids.every((value: unknown) => Number.isSafeInteger(value)
      && Number(value) >= 0), 'Malformed tokenizer input row')
  const actual = tokenizer.tokenIds(row.template, row.text)
  tokenHash.update(JSON.stringify({ id: row.id, ids: actual }) + '\n')
  const first = actual.findIndex((id, index) => id !== row.ids[index])
  if (first !== -1 || actual.length !== row.ids.length) {
    mismatchCount++
    if (mismatches.length < 20) mismatches.push({ id: row.id,
      first_difference: first === -1 ? actual.length : first,
      expected: row.ids, actual })
  }
  checked++
}
// JSONL separates records with LF only. Node readline also treats Unicode
// separators as newlines, although U+2028/U+2029 are valid inside JSON strings.
const decoder = new TextDecoder('utf-8', { fatal: true })
let pending = ''
for await (const chunk of inputStream) {
  rawHash.update(chunk)
  pending += decoder.decode(chunk, { stream: true })
  let newline: number
  while ((newline = pending.indexOf('\n')) !== -1) {
    checkLine(pending.slice(0, newline))
    pending = pending.slice(newline + 1)
  }
  assert(pending.length < 1024 * 1024, 'Tokenizer input row exceeds bound')
}
pending += decoder.decode()
if (pending) checkLine(pending)
assert(checked > 0, 'No tokenizer inputs')
process.stdout.write(JSON.stringify({ schema_version: 1, scope: 'worker-tokenizer-only',
  status: mismatchCount === 0 ? 'passed' : 'failed', checked, mismatch_count: mismatchCount,
  input_sha256: rawHash.digest('hex'), token_ids_sha256: tokenHash.digest('hex'),
  implementation_sha256: createHash('sha256').update(readFileSync(process.argv[1])).digest('hex'),
  vocab_sha256: vocabSha,
  node: process.version, unicode: process.versions.unicode,
  algorithm_version: embed.tokenizer.algorithm_version, mismatches }) + '\n')
if (mismatchCount) process.exitCode = 1
