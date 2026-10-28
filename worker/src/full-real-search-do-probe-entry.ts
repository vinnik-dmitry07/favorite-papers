import kernel from '../probe-kernel/scan.wasm'
import gateway, { StaticSearchProbe as RealObject, type RealProbeEnv } from './real-search-do-probe'

/** Genuine retained full corpus; config pins mode and the historical manifest. */
export class StaticSearchProbe extends RealObject {
  constructor(state: DurableObjectState, env: RealProbeEnv) {
    super(state, { ...env, PROBE_CORPUS_MODE: 'full', PQ_WASM: kernel })
  }
}
export default gateway
