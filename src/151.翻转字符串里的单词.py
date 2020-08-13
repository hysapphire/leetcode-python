#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

        # result = ""
        # i = 0
        # while True:
        #     while i < len(s) and s[i] == " ":
        #         i += 1

        #     if i >= len(s):
        #         break

        #     j = i
        #     while j < len(s) and s[j] != " ":
        #         j += 1

        #     if j == len(s) or s[j] == " ":
        #         result = " " + result
        #         result = s[i:j] + result
        #         i = j
            
        #     if j == len(s) - 1:
        #         break
        
        # return result[:-1]

# @lc code=end
