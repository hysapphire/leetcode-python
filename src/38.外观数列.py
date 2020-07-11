#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = self.get_next(s)

        return s

    def get_next(self, s):
        i = 0
        t = ""
        while i < len(s):
            cnt = 1
            ss = s[i]
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    cnt += 1
                    i = j
                else:
                    break
            i += 1
            t = t + str(cnt) + ss
        
        return t


        # if n == 0:
        #     return ""
        # if n == 1:
        #     return "1"
        # if n == 2:
        #     return "11"

        # s = "1"
        # for _ in range(2, n):
        #     t = ""
        #     k = 1
        #     for j in range(1, len(s)):
        #         if s[j] == s[j-1]:
        #             k += 1
        #         else:
        #             t = t + str(k) + s[j-1]
        #             k = 1
        #     t = t + str(k) + s[-1]
        #     s = t
        
        # return s

# @lc code=end

