#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        f = [[float("inf")] * (n + 1) for _ in range((m + 1))]

        f[m][n-1] = f[m-1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if min(f[i+1][j], f[i][j+1]) - dungeon[i][j] < 1:
                    f[i][j] = 1
                else:
                    f[i][j] = min(f[i+1][j], f[i][j+1]) - dungeon[i][j]

        return f[0][0]

# @lc code=end

