#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        C = [-1 for _ in range(n)]
        result = []
        self.dfs(C, result, n, 0)
        return result

    def dfs(self, C, result, n, row):
        if row == n:
            t = []
            for i in range(n):
                t.append("." * C[i] + "Q" + "." * (n-C[i]-1))
            result.append(t)
            return
        
        for i in range(n):
            if self.is_valid(C, row, i):
                C[row] = i
                self.dfs(C, result, n, row + 1)
                C[row] = -1

    def is_valid(self, C, row, col):
        for i in range(len(C)):
            if C[i] == -1:
                continue
            if i == row or C[i] == col or abs(i - row) == abs(C[i] - col):
                return False
        return True





    #     board = ["." * n for _ in range(n)]
    #     print (board)
    #     result = []
    #     index = []
    #     self.dfs(board, index, result, n, 0)
    #     return result

    # def dfs(self, board, index, result, n, row):
    #     if row == n:
    #         result.append(board[:])
    #         return

    #     for i in range(n):
    #         if any([row == idx[0] or i == idx[1] or abs(idx[0] - row) == abs(idx[1] - i) for idx in index]):
    #             continue

    #         board[row] = "." * i + "Q" + "." * (n-i-1)
    #         self.dfs(board, index + [(row, i)], result, n, row + 1)
    #         board[row] = "." * n

    #     return True

# @lc code=end

