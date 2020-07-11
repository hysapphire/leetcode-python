#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for s in strs:
            if not s:
                return ""

        max_len = 0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return strs[0][0:max_len]
            max_len += 1
        
        return strs[0][0:max_len]


        # most_right = len(strs[0])
        # for i in range(1, len(strs)):
        #     most_right = min(most_right, len(strs[i]))
        #     for j in range(len(strs[i])):
        #         if j < len(strs[0]) and strs[i][j] != strs[0][j]:
        #             most_right = min(most_right, j)
        #             break
        
        # return strs[0][0: most_right]

# @lc code=end

