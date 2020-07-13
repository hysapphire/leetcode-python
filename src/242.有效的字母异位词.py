#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for ss in s:
            d[ss] = d.get(ss, 0) + 1
        for tt in t:
            if tt not in d:
                return False
            d[tt] -= 1
            if d[tt] < 0:
                return False
        return True

# @lc code=end

