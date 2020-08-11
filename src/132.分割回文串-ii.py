#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        f = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    f[i][j] = True
                elif j - 1 == i:
                    f[i][j] = s[i] == s[j]
                else:
                    f[i][j] = f[i+1][j-1] and s[i] == s[j]
        
        dp = [len(s) for _ in range(len(s))]

        for i in range(len(s)):
            if f[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if f[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]

# @lc code=end

