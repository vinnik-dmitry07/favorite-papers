import kernel from '../probe-kernel/scan.wasm'
import gateway, { PublicSearch as PublicObject, type PublicSearchEnv } from './public-search'

export class PublicSearch extends PublicObject {
  constructor(state: DurableObjectState, env: PublicSearchEnv) {
    super(state, { ...env, PQ_WASM: kernel })
  }
}
export default gateway
