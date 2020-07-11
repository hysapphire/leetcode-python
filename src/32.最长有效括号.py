#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # max_len = 0
        # f = [[False for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s) - 1, -1, -1):
        #     match_j = []
        #     for j in range(i + 1, len(s)):
        #         if j - i == 1:
        #             f[i][j] = s[i] == "(" and s[j] == ")"
        #         else:
        #             f[i][j] = s[i] == "(" and s[j] == ")" and f[i+1][j-1]
        #             for k in match_j:
        #                 if f[i][j]:
        #                     break
        #                 f[i][j] = f[i][j] or f[k + 1][j]

        #         if f[i][j]:
        #             max_len = max(max_len, j-i+1)
        #             match_j.append(j)

        # return max_len
        max_len = 0
        f = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                j = i - f[i-1] - 1
                if j >= 0 and s[j] == "(":
                    f[i] = (i - j + 1) + (f[j - 1] if j > 0 else 0)
                    max_len = max(max_len, f[i])
        
        return max_len

# @lc code=end

