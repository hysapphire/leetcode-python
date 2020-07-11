#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        f = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i ==0 and j == 0:
                    f[j] = 0
                elif i == 0:
                    f[j] = f[j - 1]
                elif j == 0:
                    f[j] = f[j]
                else:
                    f[j] = min(f[j - 1], f[j])
                f[j] += grid[i][j]
        
        return f[-1]
# @lc code=end

