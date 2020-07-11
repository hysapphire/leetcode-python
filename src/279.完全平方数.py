#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            f[i] = float("inf")
            for j in range(i + 1):
                if i - j * j < 0:
                    break

                f[i] = min(f[i], f[i - j * j] + 1)
        
        return f[-1]

# @lc code=end

