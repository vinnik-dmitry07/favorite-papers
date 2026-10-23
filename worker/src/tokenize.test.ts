import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { describe, expect, it } from 'vitest'

import { canonicalJson, sha256Hex, signatures, vectorIdOf } from './signatures'
import { WordPieceTokenizer } from './tokenize'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')

describe('tokenizer', () => {
  const vocab = readFileSync(resolve(root, 'tokenizer/vocab.txt'), 'utf8')
  const tokenizer = new WordPieceTokenizer(vocab)
  const fixtures = JSON.parse(readFileSync(resolve(root, 'fixtures/token_ids.json'), 'utf8')) as {
    text: string
    template: string
    ids: number[]
  }[]

  it('matches the pinned BertTokenizer fixture', () => {
    expect(fixtures.length).toBeGreaterThan(0)
    for (const row of fixtures) {
      expect(tokenizer.tokenIds(row.template, row.text)).toEqual(row.ids)
    }
  })

  it('does not silently drop the special tokens', () => {
    const ids = tokenizer.tokenIds('', 'Hello, world!')
    expect(ids[0]).toBe(101)
    expect(ids[ids.length - 1]).toBe(102)
  })
})

describe('signatures', () => {
  it('matches the Python canonical hashes', async () => {
    expect(canonicalJson({ b: 1, a: 'café' })).toBe('{"a":"café","b":1}')
    const sig = await signatures()
    expect(sig.build).toBe('8cec41af54e9f4bb7432061c6d77bb5cad8c7f9513b2ce209edd5a638b4476e5')
    expect(sig.embedding).toBe('df5126063ec2f6589a0b994d6b7ebaaed8767dd49adb742803ab02b8a666cefe')
    expect(await vectorIdOf('a', 'arxiv:1', 0)).toBe(
      '526d07a2ae9159f141b8705db3413fcf7c7bc311fdf272de1150530e03f0bb75',
    )
    expect(await sha256Hex('abc')).toHaveLength(64)
  })
})

it('keeps greedy WordPiece behavior on long words and supplementary Unicode', () => {
  const vocabulary = ['[UNK]', '[CLS]', '[SEP]', 'q', '##q', '🧪', '##🧪']
  const tokenizer = new WordPieceTokenizer(vocabulary.join('\n'))
  function reference(word: string) {
    const chars = Array.from(word)
    if (chars.length > 100) return [0]
    const result: number[] = []
    for (let start = 0; start < chars.length;) {
      let end = chars.length
      while (end > start && !vocabulary.includes((start ? '##' : '') + chars.slice(start, end).join(''))) end--
      if (end === start) return [0]
      result.push(vocabulary.indexOf((start ? '##' : '') + chars.slice(start, end).join('')))
      start = end
    }
    return result
  }
  for (const suffix of ['z', '🧪', 'q']) for (const n of [0, 1, 50, 99, 100]) {
    const word = 'q'.repeat(n) + suffix
    expect(tokenizer.tokenIds('', word)).toEqual([1, ...reference(word), 2])
  }
})
