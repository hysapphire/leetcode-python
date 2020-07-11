#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "": return s == ""
        
        if len(p) == 1:
            return len(s) == 1 and (p[0] == s[0] or p[0] == ".")
        
        if p[1] != "*":
            return len(s) > 0 and (p[0] == s[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])
        else:
            return self.isMatch(s, p[2:]) or len(s) > 0 and (p[0] == s[0] or p[0] == ".") and self.isMatch(s[1:], p)
            # while len(s) > 0 and (p[0] == s[0] or p[0] == "."):
            #     if self.isMatch(s, p[2:]):
            #         return True
            #     s = s[1:]
            # return self.isMatch(s, p[2:])

# @lc code=end

