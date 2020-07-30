#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(9):
                        board[i][j] = str(k + 1)
                        if self.check_valid(board, i, j) and self.solveSudoku(board):
                            return True
                        board[i][j] = "."
                    return False
        
        return True

    def check_valid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        
        for i in range(9):
            if i != y and board[x][i] == board[x][y]:
                return False
        
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if i != x and j != y and board[i][j] == board[x][y]:
                    return False
        
        return True

# @lc code=end

