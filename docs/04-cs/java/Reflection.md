# Refletion

#### 定義

Java Reflection 是 Java 提供的一種在執行時檢查和操作類、方法、字段等程式結構的機制，允許程式動態地獲取類的資訊並進行操作。

#### 底層原理

基於 JVM 的 ClassLoader 和 MetaSpace，透過 Class 物件存儲類的元資料資訊，利用 Method、Field、Constructor 等反射類來操作物件，所有反射操作最終都會呼叫 native 方法與 JVM 互動。

#### 使用場景

- 框架開發（Spring、Hibernate）
- 動態代理
- 序列化/反序列化
- 註解處理
- 測試工具
- 配置檔案解析

#### 實際例子

Spring 框架中的依賴注入，掃描帶有 @Component 註解的類，透過反射創建 Bean 實例，找到 @Autowired 字段並注入對應的依賴物件。

```java
Class<?> clazz = Class.forName("com.example.UserService");
Object instance = clazz.getDeclaredConstructor().newInstance();
Field field = clazz.getDeclaredField("userDao");
field.setAccessible(true);
field.set(instance, userDaoInstance);
```

#### 優缺點比較

- 優點：提供動態性和靈活性、支援通用框架開發、程式碼復用性高
- 缺點：效能較差（比直接呼叫慢 10-100 倍）、破壞封裝性、編譯時無法檢查錯誤、增加程式碼複雜度

#### 與類似技術比較

- vs 註解處理器(編譯時處理 vs 執行時處理)
- vs 動態代理(Reflection 是基礎技術，動態代理是應用)
- vs 位元組碼操作(ASM、Javassist 效能更好但複雜度更高)

#### 最佳實踐

快取 Class、Method、Field 物件避免重複獲取、妥善處理 ReflectiveOperationException、考慮安全管理器限制、在效能敏感場景謹慎使用、搭配 setAccessible(true) 訪問私有成員時要注意安全風險。








