#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for ss in s:
            num = num * 26 + int(ord(ss) - ord("A") + 1)
        return num

# @lc code=end

