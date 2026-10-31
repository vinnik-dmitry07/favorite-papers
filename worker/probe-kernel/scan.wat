(module
  (memory (export "memory") 1 1024)
  ;; Float64 lookup scores, four independent accumulators. All offsets/lengths
  ;; are validated by the TypeScript caller before entering this module.
  (func (export "pq") (param $codes i32) (param $lut i32) (param $out i32)
    (param $count i32) (param $m i32) (param $k i32)
    (local $i i32) (local $j i32) (local $table i32)
    (local $a f64) (local $b f64) (local $c f64) (local $d f64)
    (block $end (loop $rows
      (br_if $end (i32.ge_u (local.get $i) (local.get $count)))
      (local.set $j (i32.const 0)) (local.set $table (local.get $lut))
      (local.set $a (f64.const 0)) (local.set $b (f64.const 0))
      (local.set $c (f64.const 0)) (local.set $d (f64.const 0))
      (block $tail (loop $four
        (br_if $tail (i32.gt_u (i32.add (local.get $j) (i32.const 4)) (local.get $m)))
        (local.set $a (f64.add (local.get $a) (f64.load (i32.add (local.get $table) (i32.shl (i32.load8_u (local.get $codes)) (i32.const 3))))))
        (local.set $table (i32.add (local.get $table) (i32.shl (local.get $k) (i32.const 3))))
        (local.set $b (f64.add (local.get $b) (f64.load (i32.add (local.get $table) (i32.shl (i32.load8_u offset=1 (local.get $codes)) (i32.const 3))))))
        (local.set $table (i32.add (local.get $table) (i32.shl (local.get $k) (i32.const 3))))
        (local.set $c (f64.add (local.get $c) (f64.load (i32.add (local.get $table) (i32.shl (i32.load8_u offset=2 (local.get $codes)) (i32.const 3))))))
        (local.set $table (i32.add (local.get $table) (i32.shl (local.get $k) (i32.const 3))))
        (local.set $d (f64.add (local.get $d) (f64.load (i32.add (local.get $table) (i32.shl (i32.load8_u offset=3 (local.get $codes)) (i32.const 3))))))
        (local.set $table (i32.add (local.get $table) (i32.shl (local.get $k) (i32.const 3))))
        (local.set $codes (i32.add (local.get $codes) (i32.const 4)))
        (local.set $j (i32.add (local.get $j) (i32.const 4))) (br $four)))
      (block $done (loop $rest
        (br_if $done (i32.ge_u (local.get $j) (local.get $m)))
        (local.set $a (f64.add (local.get $a) (f64.load (i32.add (local.get $table) (i32.shl (i32.load8_u (local.get $codes)) (i32.const 3))))))
        (local.set $codes (i32.add (local.get $codes) (i32.const 1)))
        (local.set $table (i32.add (local.get $table) (i32.shl (local.get $k) (i32.const 3))))
        (local.set $j (i32.add (local.get $j) (i32.const 1))) (br $rest)))
      (f64.store (i32.add (local.get $out) (i32.shl (local.get $i) (i32.const 3)))
        (f64.add (f64.add (local.get $a) (local.get $b)) (f64.add (local.get $c) (local.get $d))))
      (local.set $i (i32.add (local.get $i) (i32.const 1))) (br $rows))))

  (func (export "int8") (param $vectors i32) (param $query i32) (param $norms i32)
    (param $out i32) (param $ids i32) (param $count i32) (param $dims i32)
    (local $i i32) (local $j i32) (local $row i32) (local $ptr i32) (local $sum f64)
    (block $end (loop $rows
      (br_if $end (i32.ge_u (local.get $i) (local.get $count)))
      (local.set $row (if (result i32) (i32.eqz (local.get $ids))
        (then (local.get $i)) (else (i32.load (i32.add (local.get $ids) (i32.shl (local.get $i) (i32.const 2)))))))
      (local.set $ptr (i32.add (local.get $vectors) (i32.mul (local.get $row) (local.get $dims))))
      (local.set $j (i32.const 0)) (local.set $sum (f64.const 0))
      (block $done (loop $dot
        (br_if $done (i32.ge_u (local.get $j) (local.get $dims)))
        (local.set $sum (f64.add (local.get $sum) (f64.mul
          (f64.convert_i32_s (i32.load8_s (i32.add (local.get $ptr) (local.get $j))))
          (f64.load (i32.add (local.get $query) (i32.shl (local.get $j) (i32.const 3)))))))
        (local.set $j (i32.add (local.get $j) (i32.const 1))) (br $dot)))
      (f64.store (i32.add (local.get $out) (i32.shl (local.get $i) (i32.const 3)))
        (f64.mul (local.get $sum) (f64.load (i32.add (local.get $norms) (i32.shl (local.get $row) (i32.const 3))))))
      (local.set $i (i32.add (local.get $i) (i32.const 1))) (br $rows))))
  (func (export "binary") (param $bits i32) (param $query i32) (param $out i32)
    (param $count i32) (param $words i32)
    (local $i i32) (local $j i32) (local $sum i32)
    (block $end (loop $rows
      (br_if $end (i32.ge_u (local.get $i) (local.get $count)))
      (local.set $j (i32.const 0)) (local.set $sum (i32.const 0))
      (block $done (loop $word
        (br_if $done (i32.ge_u (local.get $j) (local.get $words)))
        (local.set $sum (i32.add (local.get $sum) (i32.popcnt (i32.xor
          (i32.load (local.get $bits)) (i32.load (i32.add (local.get $query) (i32.shl (local.get $j) (i32.const 2))))))))
        (local.set $bits (i32.add (local.get $bits) (i32.const 4)))
        (local.set $j (i32.add (local.get $j) (i32.const 1))) (br $word)))
      (f64.store (i32.add (local.get $out) (i32.shl (local.get $i) (i32.const 3))) (f64.neg (f64.convert_i32_u (local.get $sum))))
      (local.set $i (i32.add (local.get $i) (i32.const 1))) (br $rows))))
)
