import kernel from '../probe-kernel/scan.wasm'
import gateway, { StaticSearchProbe as ProbeObject, type DoProbeEnv } from './static-search-do-probe'

export class StaticSearchProbe extends ProbeObject {
  constructor(state: DurableObjectState, env: DoProbeEnv) {
    super(state, { ...env, PQ_WASM: kernel })
  }
}

export default gateway
