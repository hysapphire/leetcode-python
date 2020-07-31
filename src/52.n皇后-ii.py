#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        C = [-1 for _ in range(n)]
        self.cnt = 0
        self.dfs(C, n, 0)
        return self.cnt

    def dfs(self, C, n, row):
        if row == n:
            self.cnt += 1
            return
        
        for i in range(n):
            if self.is_valid(C, row, i):
                C[row] = i
                self.dfs(C, n, row + 1)
                C[row] = -1

    def is_valid(self, C, row, col):
        for i in range(len(C)):
            if C[i] == -1:
                continue
            if i == row or C[i] == col or abs(i - row) == abs(C[i] - col):
                return False
        return True

# @lc code=end

