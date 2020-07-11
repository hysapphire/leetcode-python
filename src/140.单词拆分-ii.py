#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tmp = set("".join(wordDict))
        if any([i not in tmp for i in s]):
            return []

        f = [[] for _ in range(len(s) + 1)]
        f[0] = [""]

        for i in range(1, len(s) + 1):
            fi = []
            for j in range(i):
                if s[j:i] in wordDict:
                    tmp = [t + ("" if t == "" else " ") + s[j:i] for t in f[j]]
                    fi.extend(tmp)
            f[i] = fi
        
        return f[-1]




    #     if not wordDict:
    #         return []

    #     path = []
    #     result = []
    #     word_len_list = sorted(list(set([len(word) for word in wordDict])))
    #     self.dfs(s, wordDict, 0, path, result, word_len_list)
    #     return result

    # def dfs(self, s, wordDict, idx, path, result, word_len_list):
    #     if idx >= len(s):
    #         result.append(" ".join(path))
    #         return

    #     for word_len in word_len_list:
    #         end = idx + word_len
    #         if end > len(s):
    #             continue
    #         if s[idx:end] in wordDict:
    #             self.dfs(s, wordDict, end, path + [s[idx:end]], result, word_len_list)

# @lc code=end

