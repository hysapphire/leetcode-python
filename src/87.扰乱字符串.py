#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        f = [[[False for _ in range(len(s1))] for _ in range(len(s1))] for _ in range(len(s1) + 1)]

        for i in range(len(s1)):
            for j in range(len(s1)):
                f[1][i][j] = s1[i] == s2[j]
        
        for n in range(1, len(s1) + 1):
            for i in range(len(s1) - n + 1):
                for j in range(len(s1) - n + 1):
                    for k in range(1, n):
                        if (f[k][i][j] and f[n-k][i+k][j+k]) or (f[k][i][j+n-k] and f[n-k][i+k][j]):
                            f[n][i][j] = True
                            break
        
        return f[-1][0][0]


        # if len(s1) != len(s2):
        #     return False

        # if s1 == s2:
        #     return True
        
        # if sorted(s1) != sorted(s2):
        #     return False

        # for i in range(1, len(s1)):
        #     if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
        #         or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
        #         return True
        
        # return False

# @lc code=end

