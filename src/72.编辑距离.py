#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        f = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            f[i][0] = i
        for i in range(len(word2) + 1):
            f[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(min(f[i-1][j], f[i][j-1]), f[i-1][j-1] - 1) + 1
                else:
                    f[i][j] = min(min(f[i-1][j], f[i][j-1]), f[i-1][j-1]) + 1

        return f[-1][-1]
# @lc code=end

