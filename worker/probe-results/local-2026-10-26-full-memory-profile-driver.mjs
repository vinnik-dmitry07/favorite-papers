import { Session } from 'node:inspector'
import { readFileSync, writeFileSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { resolve } from 'node:path'
import { runMemoryHarness } from './full-memory-baseline.mjs'
const session = new Session()
session.connect()
const call = (name, args = {}) => new Promise((resolve, reject) => session.post(name, args, (error, result) => error ? reject(error) : resolve(result)))
await call('HeapProfiler.startSampling', {samplingInterval: 65536, includeObjectsCollectedByMajorGC: true, includeObjectsCollectedByMinorGC: true})
try {
  await runMemoryHarness({ assets: resolve('agent_geometry_probe'), manifestSha: createHash('sha256').update(readFileSync('agent_geometry_probe/probe.json')).digest('hex'), wasm: resolve('worker/probe-kernel/scan.wasm'), vocab: resolve('worker/tokenizer/vocab.txt'), out: resolve('full-probe-reports/memory-profiled.json'), dataLabel: 'geometry-fixture', canonical: resolve('agent_full_probe/probe.json'), threshold: 96 * 1024 * 1024 })
} finally {
  const { profile } = await call('HeapProfiler.stopSampling')
  writeFileSync('full-probe-reports/allocations.heapprofile', JSON.stringify(profile))
  session.disconnect()
}
