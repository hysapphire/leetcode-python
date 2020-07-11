#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._root
        for s in word:
            if s in node:
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        node["end"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._root
        for s in word:
            if s in node:
                node = node[s]
            else:
                return False
        
        if "end" in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._root
        for s in prefix:
            if s in node:
                node = node[s]
            else:
                return False
        
        return True

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self._list = []


    # def insert(self, word: str) -> None:
    #     """
    #     Inserts a word into the trie.
    #     """
    #     self._list.append(word)


    # def search(self, word: str) -> bool:
    #     """
    #     Returns if the word is in the trie.
    #     """
    #     for s in self._list:
    #         if s == word:
    #             return True
    #     return False


    # def startsWith(self, prefix: str) -> bool:
    #     """
    #     Returns if there is any word in the trie that starts with the given prefix.
    #     """
    #     for s in self._list:
    #         if s.startswith(prefix):
    #             return True
        
    #     return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

