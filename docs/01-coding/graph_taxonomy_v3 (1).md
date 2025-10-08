# LeetCode 圖論問題分類架構 v3.1（精簡版）

## 設計原則 (Design Principles)

### 分類維度 (Classification Dimensions)
1. **按問題目標分類** - 主要維度（連通性、路徑、結構分析等）
2. **按具體問題細分** - 次要維度
3. **變化題標註** - 結合其他算法的複合問題

### 避免重疊原則
- 每道題目只出現在一個主分類下
- 算法工具作為解法標註，不作為主分類
- 複合算法問題歸入主要問題類型，標註為"變化題"

---

## 一、連通性問題 (Connectivity Problems)

### 1.1 連通分量計數 (Connected Components Counting)
**目標**: 計算圖中獨立連通區域的數量
**核心算法**: DFS、BFS、Union-Find

#### 一般圖連通分量
- 547. Number of Provinces (朋友圈)
- 323. Number of Connected Components in an Undirected Graph

#### 網格連通分量  
- 200. Number of Islands (島嶼數量) ⭐
- 1254. Number of Closed Islands (封閉島嶼數量)
- 1020. Number of Enclaves (飛地的數量)
- 695. Max Area of Island (島嶼的最大面積)
- 1905. Count Sub Islands (統計子島嶼)
- 463. Island Perimeter (島嶼周長)

#### 帶約束的連通分量
- 1559. Detect Cycles in 2D Grid (網格中的環)
- 959. Regions Cut By Slashes (斜槓分割區域)

### 1.2 連通性判定 (Connectivity Detection)
**目標**: 判斷兩點間或整圖的連通性

#### 靜態連通性判定
- 1971. Find if Path Exists in Graph
- 261. Graph Valid Tree

#### 動態連通性維護
- 1319. Number of Operations to Make Network Connected
- 990. Satisfiability of Equality Equations
- 1697. Checking Existence of Edge Length Limited Paths

### 1.3 區域變換 (Region Transformation)
**目標**: 基於連通性對區域進行標記或變換

#### 邊界處理類
- 130. Surrounded Regions (被圍繞的區域)
- 417. Pacific Atlantic Water Flow (太平洋大西洋水流)

#### 填充變換類
- 733. Flood Fill (圖像渲染)
- 1034. Coloring A Border (邊界著色)

---

## 二、路徑問題 (Path Problems)

### 2.1 路徑存在性 (Path Existence)
**目標**: 判斷是否存在滿足條件的路徑
**核心算法**: DFS、BFS

- 797. All Paths From Source to Target
- 1059. All Paths from Source Lead to Destination
- 1462. Course Schedule IV

### 2.2 最短路徑 (Shortest Path)

#### 2.2.1 無權圖最短路徑
**核心算法**: BFS

##### 狀態轉換類
- 127. Word Ladder (單詞接龍) ⭐
- 433. Minimum Genetic Mutation (最小基因變化)
- 752. Open the Lock (打開轉盤鎖)

##### 網格最短路徑
- 1091. Shortest Path in Binary Matrix
- 1926. Nearest Exit from Entrance in Maze
- 1730. Shortest Path to Get Food

##### 網格最短路徑 - 變化題
- 1293. Shortest Path in a Grid with Obstacles Elimination (+ DP)

##### 多源最短路徑
- 994. Rotting Oranges (腐爛的橘子) ⭐
- 542. 01 Matrix
- 1162. As Far from Land as Possible (地圖分析)
- 317. Shortest Distance from All Buildings
- 296. Best Meeting Point
- 1765. Map of Highest Peak

#### 2.2.2 加權圖最短路徑
**核心算法**: Dijkstra、Bellman-Ford

##### 單源最短路徑
- 743. Network Delay Time (網絡延遲時間) ⭐
- 1514. Path with Maximum Probability (最大概率路徑)

##### 單源最短路徑 - 變化題
- 1631. Path With Minimum Effort (最小體力消耗路徑) ⭐ (+ Binary Search)
- 1102. Path With Maximum Minimum Value (+ Binary Search)
- 778. Swim in Rising Water (+ Binary Search)

##### 帶約束最短路徑
- 787. Cheapest Flights Within K Stops (K站中轉內最便宜航班)
- 1928. Minimum Cost to Reach Destination in Time
- 2045. Second Minimum Time to Reach Destination

##### 帶約束最短路徑 - 變化題
- 1786. Number of Restricted Paths From First to Last Node (+ DP)

##### 全源最短路徑
- 1334. Find the City With the Smallest Number of Neighbors (Floyd-Warshall)
- 1617. Count Subtrees With Max Distance Between Cities

### 2.3 特殊路徑問題 (Special Path Problems)

#### 路徑計數
- 1976. Number of Ways to Arrive at Destination
- 62. Unique Paths
- 63. Unique Paths II

#### 路徑計數 - 變化題
- 1575. Count All Possible Routes (+ DP)
- 980. Unique Paths III (哈密頓路徑 + DP)

#### 特殊約束路徑
- 1129. Shortest Path with Alternating Colors (交替顏色最短路徑)
- 1368. Minimum Cost to Make at Least One Valid Path in a Grid

#### 訪問所有節點
- 847. Shortest Path Visiting All Nodes (狀態壓縮) ⭐

#### 訪問所有節點 - 變化題
- 943. Find the Shortest Superstring (+ DP)
- 1125. Smallest Sufficient Team (狀態壓縮 + DP)

---

## 三、圖結構分析 (Graph Structure Analysis)

### 3.1 環檢測 (Cycle Detection)
**目標**: 檢測圖中是否存在環

#### 有向圖環檢測
**核心算法**: DFS + 三色標記法
- 207. Course Schedule (課程表) ⭐
- 802. Find Eventual Safe States

#### 無向圖環檢測  
**核心算法**: DFS、Union-Find
- 684. Redundant Connection (冗餘連接) ⭐
- 685. Redundant Connection II

### 3.2 拓撲排序 (Topological Sorting)
**前提**: 有向無環圖 (DAG)
**核心算法**: Kahn算法(BFS)、DFS

#### 課程安排類
- 207. Course Schedule
- 210. Course Schedule II ⭐
- 630. Course Schedule III
- 1462. Course Schedule IV

#### 依賴關係類
- 269. Alien Dictionary (外星詞典)
- 1136. Parallel Courses
- 2115. Find All Possible Recipes from Given Supplies

### 3.3 強連通分量 (Strongly Connected Components)
**核心算法**: Tarjan、Kosaraju
- 1192. Critical Connections in a Network (Tarjan求橋) ⭐

### 3.4 二分圖判定 (Bipartite Detection)
**核心算法**: BFS/DFS 染色法
- 785. Is Graph Bipartite? ⭐
- 886. Possible Bipartition
- 1042. Flower Planting With No Adjacent

---

## 四、圖優化問題 (Graph Optimization Problems)

### 4.1 最小生成樹 (Minimum Spanning Tree)
**核心算法**: Kruskal、Prim
- 1135. Connecting Cities With Minimum Cost
- 1584. Min Cost to Connect All Points ⭐
- 1489. Find Critical and Pseudo-Critical Edges in MST
- 1168. Optimize Water Distribution in a Village

#### 最小生成樹 - 變化題
- 1042. Flower Planting With No Adjacent (+ Greedy)

### 4.2 並查集應用 (Union-Find Applications)
**目標**: 動態維護集合的合併和查詢

#### 集合合併類
- 721. Accounts Merge (帳戶合併) ⭐
- 839. Similar String Groups
- 1202. Smallest String With Swaps

#### 等價關係類
- 990. Satisfiability of Equality Equations
- 952. Largest Component Size by Common Factor
- 1632. Rank Transform of a Matrix

#### 路徑查詢類
- 1697. Checking Existence of Edge Length Limited Paths
- 1724. Checking Existence of Edge Length Limited Paths

### 4.3 匹配問題 (Matching Problems)
- 1066. Campus Bikes II
- 1349. Maximum Students Taking Exam (二分圖最大匹配)

---

## 五、特殊圖結構 (Special Graph Structures)

### 5.1 樹結構 (Tree Structures)
**特點**: 無環連通圖

#### 樹的性質
- 310. Minimum Height Trees (最小高度樹)
- 1245. Tree Diameter

#### 樹上統計
- 834. Sum of Distances in Tree
- 1615. Maximal Network Rank

### 5.2 有向無環圖 (DAG)
**特點**: 有向且無環

#### DAG 路徑問題
- 329. Longest Increasing Path in a Matrix ⭐

#### DAG 路徑問題 - 變化題
- 1289. Minimum Falling Path Sum II (+ DP)

### 5.3 歐拉路徑與哈密頓路徑 (Eulerian & Hamiltonian Paths)

#### 歐拉路徑 (每條邊恰好經過一次)
**核心算法**: Hierholzer算法
- 753. Cracking the Safe
- 332. Reconstruct Itinerary ⭐

#### 哈密頓路徑 (每個節點恰好經過一次)
**核心算法**: 狀態壓縮DP、回溯
- 980. Unique Paths III
- 847. Shortest Path Visiting All Nodes

---

## 六、高級搜索技術 (Advanced Search Techniques)

### 6.1 狀態空間搜索 (State Space Search)

#### 狀態壓縮搜索
**技巧**: 用位運算壓縮狀態
- 847. Shortest Path Visiting All Nodes
- 943. Find the Shortest Superstring
- 1125. Smallest Sufficient Team

#### 雙向搜索
**適用**: 起點終點已知，搜索空間大
- 127. Word Ladder (優化解法)
- 752. Open the Lock
- 1298. Maximum Candies You Can Get from Boxes

### 6.2 記憶化搜索 (Memoized Search)
- 329. Longest Increasing Path in a Matrix

#### 記憶化搜索 - 變化題
- 1575. Count All Possible Routes (+ DP)

### 6.3 特殊搜索應用 (Special Search Applications)

#### 遊戲與謎題
- 752. Open the Lock
- 773. Sliding Puzzle
- 753. Cracking the Safe
- 289. Game of Life (生命遊戲)
- 1655. Distribute Repeating Integers

#### 圖重建與序列化
- 133. Clone Graph
- 138. Copy List with Random Pointer
- 1153. String Transforms Into Another String

