import { readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import wabtFactory from 'wabt'
const wabt = await wabtFactory()
const source = new URL('./scan.wat', import.meta.url)
const module = wabt.parseWat('scan.wat', await readFile(source, 'utf8'))
module.resolveNames()
module.validate()
const bytes = module.toBinary({ canonicalize_lebs: true }).buffer
module.destroy()
const expected = (await readFile(new URL('./scan.sha256', import.meta.url), 'utf8')).trim()
const actual = createHash('sha256').update(bytes).digest('hex')
if (actual !== expected) throw new Error('WASM output differs from the reviewed scan.sha256; review the kernel/compiler change before updating the pin')
await writeFile(new URL('./scan.wasm', import.meta.url), bytes)
