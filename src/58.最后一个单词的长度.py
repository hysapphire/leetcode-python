#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        j = i

        while i >= 0 and s[i] != " ":
            i -= 1

        return j - i
        
# @lc code=end

