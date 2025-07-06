# 挑戰: 高併發防重複與一致性設計

## 問題背景：

在高併發場景下（如錢包提領、秒殺搶購），需要避免：
- 重複提交
- 餘額超發
- 扣款錯亂
- 保證一致性與高效能

## 消息佇列層（Kafka）

- Message Key：使用 requestId 或 userId:activityId
- Producer 端
    - 設定 `acks=all`
    - `enable.idempotence=true`
- Consumer 端
    - 消費時去重（RocksDB / Redis / compact topic）
    - 重試機制，保證 at-least-once or exactly-once

## 快取層（Redis）

- 防重複操作 `SET userId:activityId "processing" NX EX 5`


## 資料庫層（MySQL）

 