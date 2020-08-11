#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or (endWord not in wordList):
            return []

        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + "*" + word[i+1:]].append(word)
        
        q = [[beginWord]]
        visited = set()
        found = False
        result = []
        while q:
            if found:
                return result

            for path in q:
                visited.add(path[-1])
            
            tmp = []
            for path in q:
                word = path[-1]
                for i in range(len(word)):
                    next_words = d[word[:i] + "*" + word[i+1:]]
                    for next_word in next_words:
                        if next_word == endWord:
                            result.append(path + [endWord])
                            found = True
                            continue
                        if next_word not in visited:
                            tmp.append(path + [next_word])
            q = tmp
        
        return result



        # if not beginWord or not endWord or not wordList or (endWord not in wordList):
        #     return []

        # d = defaultdict(list)
        # for word in wordList:
        #     for i in range(len(word)):
        #         d[word[:i] + "*" + word[i+1:]].append(word)
        
        # q = deque([[(beginWord, 1)]])
        # visited = {beginWord: 1}
        # min_len = float("inf")
        # result = []
        # while q:
        #     path = q.popleft()
        #     word, level = path[-1]
        #     if level >= min_len:
        #         return result
        #     for i in range(len(word)):
        #         next_words = d[word[:i] + "*" + word[i+1:]]
        #         for next_word in next_words:
        #             if next_word == endWord:
        #                 min_len = min(min_len, level + 1)
        #                 result.append([p[0] for p in path] + [endWord])
        #                 continue
        #             if next_word in visited and visited[next_word] < level + 1:
        #                 continue
        #             q.append(path + [(next_word, level + 1)])
        #             visited[next_word] = level + 1
        
        # return result

# @lc code=end

