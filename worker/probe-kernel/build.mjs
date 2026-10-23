import { readFile, writeFile } from 'node:fs/promises'
import wabtFactory from 'wabt'
const wabt = await wabtFactory()
const source = new URL('./scan.wat', import.meta.url)
const module = wabt.parseWat('scan.wat', await readFile(source, 'utf8'))
module.resolveNames()
module.validate()
await writeFile(new URL('./scan.wasm', import.meta.url), module.toBinary({ canonicalize_lebs: true }).buffer)
module.destroy()
