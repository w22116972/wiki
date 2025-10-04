"""
2658. Maximum Number of Fish in a Grid
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""
from collections import deque
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] > 0:
                    queue = deque()
                    queue.append((i, j))
                    visited.add((i, j))
                    fish = 0
                    while queue:
                        (x, y) = queue.popleft()
                        fish += grid[x][y]

                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] > 0:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                    max_fish = max(max_fish, fish)
        return max_fish