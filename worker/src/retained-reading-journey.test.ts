import { readFileSync } from 'node:fs'
import { gunzipSync } from 'node:zlib'
import { describe, expect, it, vi } from 'vitest'
import { createJourneyAdapter } from '../probe-kernel/agent-journey'
import { readSeeds } from '../probe-kernel/retained-reading-journey'

const evidence = readFileSync('probe-results/retained-smoke-40806851930.evidence.json.gz')

describe('retained live-response reading recovery', () => {
  it('preserves the two exact response strings and their question pairing', () => {
    const original = JSON.parse(JSON.parse(gunzipSync(evidence).toString('utf8')).original_run_report_utf8)
    const searches = original.requests.filter((row: any) => row.kind === 'new_query')
    const seeds = readSeeds(evidence)
    expect(seeds.map((seed: any) => seed.id)).toEqual(['recovery-01', 'recovery-02'])
    expect(seeds.map((seed: any) => seed.question_id)).toEqual(['live-smoke-1', 'live-smoke-2'])
    for (let i = 0; i < seeds.length; i++) {
      expect(seeds[i].response_text).toBe(searches[i].response_text)
      expect(seeds[i].question).toBe(original.journeys[i].query)
      expect(JSON.parse(seeds[i].response_text).hits).toHaveLength(3)
    }
  })

  it('rejects altered evidence before reading historical results', () => {
    const changed = Buffer.from(evidence)
    changed[changed.length - 1] ^= 1
    expect(() => readSeeds(changed)).toThrow('evidence checksum mismatch')
  })

  it('declares k=3, counts the exact seed body and forbids semantic reformulation', async () => {
    const seed = readSeeds(evidence)[0]
    const session = { id: seed.id, question_id: seed.question_id, question: seed.question, vector_row: -1 }
    const forward = vi.fn(async () => new Response(seed.response_text))
    const adapter = createJourneyAdapter({ sessions: [session], searchKDefault: 3, forward, record: () => {} })
    const base = 'http://127.0.0.1/session/' + seed.id
    expect((await (await adapter.fetch(new Request(base + '/setup'))).json()).rest.search_k_default).toBe(3)
    const response = await adapter.fetch(new Request(base + '/v1/search?' + new URLSearchParams({ q: seed.question })))
    expect(await response.text()).toBe(seed.response_text)
    expect(response.headers.get('x-journey-delivered-code-points')).toBe(String([...seed.response_text].length))
    expect(new URL(forward.mock.calls[0][0].url).searchParams.get('k')).toBe('3')
    const denied = await adapter.fetch(new Request(base + '/v1/search?q=another+semantic+question'))
    expect(denied.status).toBe(400)
    expect(forward).toHaveBeenCalledTimes(1)
  })
})
