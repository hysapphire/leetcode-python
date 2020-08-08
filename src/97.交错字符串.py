#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        f = [False for _ in range(len(s2) + 1)]

        f[0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    f[j] = (f[j] and s1[i-1] == s3[i+j-1])

                if j > 0:
                    f[j] = (f[j-1] and s2[j-1] == s3[i+j-1]) or f[j]

        return f[len(s2)]



        # if len(s1) + len(s2) != len(s3):
        #     return False
        
        # f = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        # f[0][0] = True
        # for i in range(len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i > 0:
        #             f[i][j] = (f[i-1][j] and s1[i-1] == s3[i+j-1]) or f[i][j]

        #         if j > 0:
        #             f[i][j] = (f[i][j-1] and s2[j-1] == s3[i+j-1]) or f[i][j]

        # return f[len(s1)][len(s2)]



        # if len(s1) + len(s2) != len(s3):
        #     return False
        # if not s1:
        #     return s2 == s3
        # if not s2:
        #     return s1 == s3
        
        # f = [[[False for _ in range(len(s3) + 1)] for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        # for i in range(len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i == 0 and j == 0:
        #             f[i][j][i+j] = True
        #         elif i == 0:
        #             f[i][j][i+j] = True if (f[i][j-1][i+j-1] and s2[j-1] == s3[i+j-1]) else False
        #         elif j == 0:
        #             f[i][j][i+j] = True if (f[i-1][j][i+j-1] and s1[i-1] == s3[i+j-1]) else False
        #         else:
        #             if (f[i-1][j][i+j-1] and s1[i-1] == s3[i+j-1]) or (f[i][j-1][i+j-1] and s2[j-1] == s3[i+j-1]):
        #                 f[i][j][i+j] = True

        # return f[len(s1)][len(s2)][len(s3)]

# @lc code=end

