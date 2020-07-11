#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        f = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               if grid[i][j] == "1" and f[i][j] == 0:
                   num += 1
                   self.fill(grid, f, i, j, len(grid), len(grid[0]), num)
        
        return num

    def fill(self, grid, f, i, j, m, n, num):
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] == "0" or f[i][j] > 0:
            return

        if grid[i][j] == "1":
            f[i][j] = num
        self.fill(grid, f, i + 1, j, m, n, num)
        self.fill(grid, f, i - 1, j, m, n, num)
        self.fill(grid, f, i, j + 1, m, n, num)
        self.fill(grid, f, i, j - 1, m, n, num)
# @lc code=end

