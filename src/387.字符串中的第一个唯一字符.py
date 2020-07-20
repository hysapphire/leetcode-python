#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for ss in s:
            d[ss] = d.get(ss, 0) + 1

        for i, ss in enumerate(s):
            if d[ss] == 1:
                return i

        return -1
            
# @lc code=end

