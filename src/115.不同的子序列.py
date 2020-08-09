#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        f = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            f[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i-1][j-1] + f[i-1][j]
                else:
                    f[i][j] = f[i-1][j]
        
        return f[-1][-1]

        # if not s or not t:
        #     return 0

        # f = [[0 for _ in range(len(t))] for _ in range(len(s))]

        # f[0][0] = 1 if s[0] == t[0] else 0
        # for i in range(1, len(s)):
        #     if s[i] == t[0]:
        #         f[i][0] = f[i-1][0] + 1
        #     else:
        #         f[i][0] = f[i-1][0]

        # for i in range(1, len(s)):
        #     for j in range(1, len(t)):
        #         if s[i] == t[j]:
        #             f[i][j] = f[i-1][j-1] + f[i-1][j]
        #         else:
        #             f[i][j] = f[i-1][j]
        
        # return f[-1][-1]
        
# @lc code=end

