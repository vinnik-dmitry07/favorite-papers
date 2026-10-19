import kernel from '../probe-kernel/scan.wasm'
import probe, { type ProbeEnv } from './static-search-probe'
export default {
  fetch(request: Request, env: ProbeEnv) {
    return probe.fetch(request, { ...env, PQ_WASM: kernel })
  },
}
