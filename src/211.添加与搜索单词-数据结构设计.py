#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self._d
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]

        node["EOW"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, self._d)
        
    def _search(self, word, node):
        if node == True:
            return False

        for i in range(len(word)):
            if word[i] != ".":
                if word[i] not in node:
                    return False
                node = node[word[i]]
            elif word[i] == ".":
                for v in node.values():
                    if self._search(word[i+1:], v):
                        return True
                return False
            else:
                return False
        
        if "EOW" not in node:
            return False
        else:
            return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

