# HashMap vs ConcurrentHashMap

定義：HashMap 是非執行緒安全的雜湊表實作，ConcurrentHashMap 是專為多執行緒環境設計的執行緒安全雜湊表，兩者都實作了 Map 介面。

## 底層原理

- **HashMap**：採用陣列 + 鏈表 + 紅黑樹結構，當鏈表長度超過 8 且陣列容量大於 64 時轉為紅黑樹
- **ConcurrentHashMap**：用「Node array + 鏈表/紅黑樹」結構。主要透過「CAS（Compare-And-Swap）」操作來實現無鎖化的併發寫入，只有在必要時才會對單個桶（bucket）加 synchronized 鎖。
    - 讀操作通常是無鎖的（弱一致性，可能讀到舊值）
    - 寫操作只鎖定單一桶位，避免全表鎖定
    - 適合高併發場景，能有效減少鎖競爭

## 使用場景

- **HashMap**：單執行緒環境、不需要執行緒安全的快取場景
- **ConcurrentHashMap**：多執行緒環境、需要高並發讀寫的共享資料結構、執行緒安全的快取系統

## 實際例子

在電商系統中，商品庫存管理使用 ConcurrentHashMap 儲存商品 ID 與庫存數量的映射，多個執行緒同時處理訂單時可以安全地更新庫存；而單執行緒的資料處理任務中使用 HashMap 儲存臨時計算結果。

## 優缺點比較

| 特性             | HashMap                                   | ConcurrentHashMap                                 |
|------------------|-------------------------------------------|---------------------------------------------------|
| 效能             | 更佳                                      | 略低                                              |
| 記憶體佔用       | 較少                                      | 較大                                              |
| 執行緒安全       | 否                                        | 是                                                |
| 多執行緒下風險   | 可能造成死循環                            | 支援高並發                                        |
| API 複雜度       | 較簡單                                    | 較複雜                                            |

## 與類似技術比較

| 比較對象                        | ConcurrentHashMap 優勢                                  |
|----------------------------------|--------------------------------------------------------|
| vs Hashtable                    | 效能更佳（細粒度鎖 vs 全域鎖）                         |
| vs Collections.synchronizedMap()| 並發性能更好，讀操作無需加鎖                           |
| vs Redis                        | JVM 內部資料結構，Redis 是分散式快取                   |

## 最佳實踐

- 單執行緒場景優先選擇 HashMap
- 多執行緒場景使用 ConcurrentHashMap，避免使用 Hashtable
- ConcurrentHashMap 的 size() 方法在高並發下是估算值，不要依賴精確性
- 合理設定初始容量和載入因子，避免頻繁擴容
- 使用 putIfAbsent()、replace() 等原子操作方法保證執行緒安全

## 進階加分點

- **效能數據**：在相同硬體環境下，HashMap 的純讀寫效能比 ConcurrentHashMap 快約 20-30%，但 ConcurrentHashMap 在多執行緒環境下的總體吞吐量更高。
- **個人經驗**：在我負責的訂單系統中，原本使用 HashMap + synchronized 實作執行緒安全，後來改用 ConcurrentHashMap，系統並發處理能力提升了約 40%，CPU 使用率也明顯降低。