#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 0
        f = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2:
                        f[i][j] = True
                    else:
                        f[i][j] = f[i + 1][j - 1]
                    if f[i][j]:
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            max_i = i
                            max_j = j
                else:
                    f[i][j] = False

        return s[max_i:max_j+1]
# @lc code=end

