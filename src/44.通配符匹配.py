#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        f = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        f[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                f[0][j] = True
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == "?" or s[i-1] == p[j-1]:
                    f[i][j] = f[i-1][j-1]
                elif p[j-1] == "*":
                        f[i][j] = f[i][j-1] or f[i-1][j]
                else:
                    f[i][j] = False

        return f[-1][-1]



    #     return self.is_match(s, p)

    # def is_match(self, s, p):
    #     if p and p[0] == "*":
    #         while p and p[0] == "*":
    #             p = p[1:]
    #         if not p:
    #             return True
    #         while s and not self.is_match(s, p):
    #             s = s[1:]
    #         return s != ""
    #     if not s or not p:
    #         return s == p
    #     if s[0] == p[0] or p[0] == "?":
    #         return self.is_match(s[1:], p[1:])
    #     return False

# @lc code=end

