#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False] * (len(s) + 1)
        f[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if f[j] and s[j: i] in wordDict:
                    f[i] = True
                    break
        
        return f[-1]

        # f = [False] * len(s)

        # for i in range(len(s)):
        #     if s[:i+1] in wordDict:
        #         f[i] = True
        #     for j in range(i):
        #         if f[j] and s[j+1:i+1] in wordDict:
        #             f[i] = True
        #             break

        # return f[len(s) - 1]

# @lc code=end

