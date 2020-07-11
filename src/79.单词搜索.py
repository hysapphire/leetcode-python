#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        is_used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, is_used, len(board), len(board[0]), i, j):
                    return True

        return False

    def dfs(self, board, word, is_used, m, n, i, j):
        if word == "":
            return True
        if i < 0 or j < 0 or i == m or j == n or is_used[i][j]:
            return False

        if board[i][j] != word[0]:
            return False
        
        is_used[i][j] = True

        flag = self.dfs(board, word[1:], is_used, m, n, i + 1, j) \
            or self.dfs(board, word[1:], is_used, m, n, i, j + 1) \
            or self.dfs(board, word[1:], is_used, m, n, i - 1, j) \
            or self.dfs(board, word[1:], is_used, m, n, i, j - 1)
        is_used[i][j] = False

        return flag

             

# @lc code=end

