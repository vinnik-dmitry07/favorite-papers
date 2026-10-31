/** Workers nodejs_compat implements the context methods used by public search. */
declare module 'node:async_hooks' {
  export class AsyncLocalStorage<T> {
    getStore(): T | undefined
    run<R>(store: T, callback: () => R): R
  }
}
