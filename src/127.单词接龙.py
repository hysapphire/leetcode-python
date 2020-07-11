#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0        

        self.length = len(beginWord)
        self.all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[0:i] + "*" + word[i+1:]].append(word)
        
        begin_queue = [(beginWord, 1)]
        end_queue = [(endWord, 1)]
        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}

        while begin_queue and end_queue:
            ans = self.ladder_length(begin_queue, begin_visited, end_visited)
            if ans is not None:
                return ans
            ans = self.ladder_length(end_queue, end_visited, begin_visited)
            if ans is not None:
                return ans

        return 0

    def ladder_length(self, queue, visited, other_visited):
        current_word, level = queue.pop(0)

        for i in range(self.length):
            next_word_list = self.all_combo_dict[current_word[0:i] + "*" + current_word[i+1:]]
            for next_word in next_word_list:
                if next_word in other_visited:
                    return level + other_visited[next_word]
                if next_word not in visited:
                    visited[next_word] = level + 1
                    queue.append((next_word, level + 1))
        
        return None




        # if endWord not in wordList or not beginWord or not endWord or not wordList:
        #     return 0

        # L = len(beginWord)
        # all_combo_dict = defaultdict(list)
        # for word in wordList:
        #     for i in range(L):
        #         all_combo_dict[word[0:i] + "*" + word[i+1:]].append(word)
        
        # queue = [(beginWord, 1)]
        # visited = {beginWord: True}
        # while queue:
        #     current_word, level = queue.pop(0)

        #     for i in range(L):
        #         next_word_list = all_combo_dict[current_word[0:i] + "*" + current_word[i+1:]]
        #         for next_word in next_word_list:
        #             if next_word == endWord:
        #                 return level + 1
        #             if next_word not in visited:
        #                 visited[next_word] = True
        #                 queue.append((next_word, level + 1))
                
        #         # all_combo_dict[current_word[0:i] + "*" + current_word[i+1:]] = []
        
        # return 0




        # self.min_len = float("inf")

        # def is_valid(w1, w2):
        #     cnt = 0
        #     for s1, s2 in zip(w1, w2):
        #         if s1 != s2:
        #             cnt += 1
        #             if cnt > 1:
        #                 return False
            
        #     return cnt == 1

        # def ladder_length(path):
        #     if path[-1] == endWord:
        #         self.min_len = min(self.min_len, len(path))
        #         return
        #     for w in wordList:
        #         if w in path:
        #             continue
        #         if is_valid(path[-1], w):
        #             ladder_length(path + [w])

        # path = [beginWord]
        # ladder_length(path)

        # return self.min_len if self.min_len != float("inf") else 0
        
# @lc code=end

