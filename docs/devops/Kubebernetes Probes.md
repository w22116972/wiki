# Kubernetes Probes

## Liveness Probe

### 用途

檢查應用程式是否陷入死鎖或無回應狀態
- 應該要快速且輕量，避免對應用程式造成負擔

### 情境

如果 Liveness Probe 檢查失敗，Kubernetes 會將容器殺掉（restart），避免應用程式進入無法恢復的錯誤狀態。

### 範例

適用於長時間運行但有可能陷入死鎖或無限循環的應用。

## Readiness Probe

### 用途

檢查容器是否「已準備好對外提供服務」。

### 情境

如果 Readiness Probe 檢查失敗，Kubernetes 會將該 Pod 從 Service 的 Endpoint 列表中移除，讓外部請求不會送到這個還沒準備好的容器。

### 範例

適用於需要初始化、載入資料或建立連線等動作的應用，確認完成準備才接受請求。

## Startup Probe

### 用途

檢查應用程式「啟動過程」是否完成。

### 情境

- 如果應用啟動時間較長，使用 Startup Probe 可以避免 Liveness Probe 過早檢查而重啟容器。
- 在 Startup Probe 通過前，Kubernetes 會暫停 Liveness 和 Readiness 的檢查。

### 範例

適用於需要較長啟動時間的大型應用

