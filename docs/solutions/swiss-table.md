# Swiss Table

## Key design

- all data (or pointers to data) is stored in one contiguous array
    - avoids the "pointer chasing" which leads to cache misses
- open addressing: if it has collision, then it uses "probing sequence" to find the next available slot
    - data layout is compact with no extra pointer overhead, which is highly beneficial for the CPU's cache locality
- SIMD
    - Control Byte Array: Swiss Table maintains a separate, extremely compact "metadata" array. Each byte in this array corresponds to a slot in the main data array and only stores the state of that slot.
    - Group Probing: When looking up a key, it doesn't check slots one by one. Instead, it uses SIMD (Single Instruction, Multiple Data) instructions to load a "group" of control bytes (typically 16) at once.
    - Parallel Comparison: It takes the top 7 bits of the target key's hash and compares them against all 16 control bytes in a single CPU instruction, instantly producing a 16-bit bitmask. This bitmask directly reveals which of the 16 slots are potential candidates for a match.

The Result: In most cases, a single SIMD operation can eliminate 15 mismatched slots, drastically reducing the number of expensive memory probes and key comparisons.

---

## Java Challenge

### Pointer Chasing

e.g. `Slot[] slots`

```
// | ref_to_s0 | ref_to_s1 | ref_to_s2 | ... |  (main array stores references/pointers)
//      |           |           |
//      V           V           V
//  Slot 0 Obj   Slot 1 Obj   Slot 2 Obj      (Slot objects in head are scattered and non-contiguous)
//    | |            | |
//    V V            V V
//  Key0, Val0     Key1, Val1               (Key/Value objects in heap are scattered and non-contiguous)
```

This is main reason why it loses to C++


---

## Swiss Table vs ConcurrentHashMap

### 優勢

#### 鎖定區域內的執行速度

一個操作的總時間 = 等待鎖的時間 + 持有鎖並執行操作的時間。

- Sharded Swiss Table：獲得鎖後，操作的是對 CPU 快取極其友好的 Swiss Table。資料在連續記憶體上，沒有指標跳躍，執行速度飛快。因此鎖的持有時間極短，迅速釋放給下一個等待者。
- CHM: 需要遍歷一個鏈結串列 or tree, 每一次指標跳躍都可能是一次昂貴的快取失誤 (Cache Miss)

#### 鎖競爭的實際機率

- 分片數量 >> CPU 核心數

#### CPU 快取的好感度 (The Cache-Friendliness)

- Swiss Table：扁平化、連續的記憶體佈局是為 CPU 快取量身定做的。一個快取行（Cache Line）可以載入多個元素或元數據，後續操作都在飛快的 L1/L2 快取中完成。
- CHM: 鏈結串列和離散的 Node 物件是快取的天敵。CPU 需要多次從慢速的主記憶體中讀取資料

