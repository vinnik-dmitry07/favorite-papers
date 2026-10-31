import kernel from '../probe-kernel/scan.wasm'
import gateway, { StaticSearchProbe as GeometryObject, type GeometryProbeEnv } from './full-geometry-do-probe'

export class StaticSearchProbe extends GeometryObject {
  constructor(state: DurableObjectState, env: GeometryProbeEnv) {
    super(state, { ...env, PQ_WASM: kernel })
  }
}
export default gateway
