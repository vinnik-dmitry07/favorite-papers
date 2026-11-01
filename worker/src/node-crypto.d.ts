// The probes enable nodejs_compat; avoid importing the full Node type surface.
declare module 'node:crypto' {
  export function timingSafeEqual(a: ArrayBufferView, b: ArrayBufferView): boolean
}
