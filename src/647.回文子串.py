#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        f = [[False for _ in range(len(s))] for _ in range(len(s))]

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i ,len(s)):
                if j - i < 2:
                    f[i][j] = s[i] == s[j]
                    if f[i][j]:
                        cnt += 1
                    continue 
                f[i][j] = f[i+1][j-1] and s[i] == s[j]
                if f[i][j]:
                    cnt += 1
        
        return cnt

# @lc code=end

