#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["end"] = word

        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    self.dfs(board, i, j, len(board), len(board[0]), trie, result)
        
        return result


    def dfs(self, board, i, j, m, n, node, result):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] not in node:
            return
        
        letter = board[i][j]
        if "end" in node[letter]:
            result.append(node[letter]["end"])
            node[letter].pop("end")
        
        board[i][j] = "#"
        
        self.dfs(board, i - 1, j, m, n, node[letter], result)
        self.dfs(board, i + 1, j, m, n, node[letter], result)
        self.dfs(board, i, j - 1, m, n, node[letter], result)
        self.dfs(board, i, j + 1, m, n, node[letter], result)

        board[i][j] = letter




    #     result = []
    #     for word in words:
    #         flag = False
    #         for i in range(len(board)):
    #             if flag:
    #                 break
    #             for j in range(len(board[0])):
    #                 if flag:
    #                     break
    #                 if board[i][j] == word[0] and self.dfs(board, word, i, j, len(board), len(board[0]), 1):
    #                     result.append(word)
    #                     flag = True
    #     return result

    # def dfs(self, board, word, i, j, m, n, idx):
    #     if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx-1]:
    #         return False

    #     if idx == len(word):
    #         return True
        
    #     board[i][j] = "#"

    #     flag =  self.dfs(board, word, i - 1, j, m, n, idx + 1) or \
    #         self.dfs(board, word, i + 1, j, m, n, idx + 1) or \
    #         self.dfs(board, word, i, j - 1, m, n, idx + 1) or \
    #         self.dfs(board, word, i, j + 1, m, n, idx + 1)
        
    #     board[i][j] = word[idx-1]

    #     return flag


# @lc code=end

