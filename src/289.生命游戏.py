#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                t = self.judge(board, i, j ,len(board), len(board[0]))
                if board[i][j] == 1:
                    if t < 2 or t > 3:
                        board[i][j] = "*"
                elif board[i][j] == 0:
                    if t == 3:
                        board[i][j] = "#"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "*":
                    board[i][j] = 0
                if board[i][j] == "#":
                    board[i][j] = 1


    def judge(self, board, i, j, m, n):
        cnt = 0
        for p in [-1, 0, 1]:
            for q in [-1, 0, 1]:
                if p == 0 and q == 0:
                    continue
                if i + p < 0 or j + q < 0 or i + p >= m or j + q >= n:
                    continue
                if board[i+p][j+q] == 1 or board[i+p][j+q] == "*":
                    cnt += 1
        return cnt
            
# @lc code=end