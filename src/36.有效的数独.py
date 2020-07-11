#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            d = set()
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in d:
                    return False
                elif board[i][j] != ".":
                    d.add(board[i][j])

        for j in range(len(board[0])):
            d = set()
            for i in range(len(board)):
                if board[i][j] != "." and board[i][j] in d:
                    return False
                elif board[i][j] != ".":
                    d.add(board[i][j])
        
        for p in range(3):
            for q in range(3):
                d = set()
                for i in range(3):
                    for j in range(3):
                        if board[p * 3 + i][q * 3 + j] != "." and board[p * 3 + i][q * 3 + j] in d:
                            return False
                        else:
                            d.add(board[p * 3 + i][q * 3 + j])
        
        return True

# @lc code=end

