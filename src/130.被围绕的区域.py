#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                is_edge = i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1
                if is_edge and board[i][j] == "O":
                    self.dfs(board, i, j, len(board), len(board[0]))
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

    def dfs(self, board, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "X" or board[i][j] == "#":
            return 

        board[i][j] = "#"
        
        self.dfs(board, i - 1, j, m, n)
        self.dfs(board, i + 1, j, m, n)
        self.dfs(board, i, j - 1, m, n)
        self.dfs(board, i, j + 1, m, n)


    # def dfs(self, board, x, y, m, n):
    #     stack = []
    #     stack.append((x, y))

    #     while stack:
    #         i, j = stack.pop(0)
    #         board[i][j] = "#"
    #         if i - 1 >= 0 and board[i-1][j] == "O":
    #             stack.append((i - 1, j))
    #             board[i-1][j] = "#"
    #         if i + 1 < m and board[i+1][j] == "O":
    #             stack.append((i + 1, j))
    #             board[i+1][j] = "#"
    #         if j - 1 >= 0 and board[i][j-1] == "O":
    #             stack.append((i, j-1))
    #             board[i][j-1] = "#"
    #         if j + 1 < n and board[i][j+1] == "O":
    #             stack.append((i, j + 1))
    #             board[i][j+1] = "#"

# @lc code=end

