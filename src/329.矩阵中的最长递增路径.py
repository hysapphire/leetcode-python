#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self._max = 0
        flag = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, len(matrix), len(matrix[0]), 1, flag)
        
        return self._max


    def dfs(self, matrix, i, j, m, n, s, flag):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        
        if flag[i][j] > 0:
            return s + flag[i][j]

        t = 0
        if i > 0 and matrix[i][j] < matrix[i-1][j]:
            t = max(t, self.dfs(matrix, i - 1, j, m, n, s, flag))
        if i < m - 1 and matrix[i][j] < matrix[i+1][j]:
            t = max(t, self.dfs(matrix, i + 1, j, m, n, s, flag))
        if j > 0 and matrix[i][j] < matrix[i][j-1]:
            t = max(t, self.dfs(matrix, i, j - 1, m, n, s, flag))
        if j < n - 1 and matrix[i][j] < matrix[i][j+1]:
            t = max(t, self.dfs(matrix, i, j + 1, m, n, s, flag))

        flag[i][j] = t

        s += t
        self._max = max(self._max, s)

        return s

# @lc code=end

