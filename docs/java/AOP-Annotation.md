# AOP and Annotation

`@Target({ElementType.TYPE, ElementType.METHOD})`
- `TYPE`: apply to `class`, `interface`, `enum`
- 定義了 AOP 中切點 (Pointcut)的目標: 掃描所有標記該Annotation的類別和方法

`@Retention(RetentionPolicy.RUNTIME)`
- 註解的生命週期: 保證 AOP 在「執行期」能看到這個標籤
  - 註解的資訊會被編譯到 `.class` 檔案中，並且在JVM執行期間也能透過Reflection機制讀取

#### 完整過程: 以 `@Transactional` 為例

1. 掃描與識別：當 Spring 容器啟動時，它會掃描所有被管理的 Bean。Spring 的交易管理功能（由 TransactionManager 驅動）會建立一個切面 (Aspect)。
2. 定義切點 (Pointcut)：這個切面中包含一個預先定義好的切點，這個切點的規則就是「尋找所有被 @Transactional 註解標記的公開方法（public method）」。
3. 建立代理 (Proxy)：對於任何符合這個切點規則的類別（即包含 @Transactional 方法的 Bean），Spring 不會直接回傳原始的物件實例。相反，它會動態地建立一個代理物件 (Proxy Object) 來包裝原始物件。
4. 方法攔截 (Interception)：當您的程式碼呼叫那個被 @Transactional 標記的方法時，實際上呼叫的是代理物件的同名方法。
5. 執行通知 (Advice)：代理物件的方法會執行「通知 (Advice)」邏輯。在這種情況下，這個通知就是交易管理邏輯（由 TransactionInterceptor 類別實現）。它會：
  1. 在呼叫真正的方法之前，開始一個交易。
  2. 呼叫原始物件的那個方法，執行您的業務邏輯。
  3. 在方法成功執行完畢之後，提交交易。
  4. 如果在執行過程中拋出了需要回滾的例外，則捕捉例外並回滾交易。