#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        f = [0] * (len(s) + 1)
        f[0] = 1
        f[1] = 1
        
        for i in range(2, len(s) + 1):
            if int(s[i-1]) == 0:
                if int(s[i-2]) == 1 or int(s[i-2]) == 2:
                    f[i] = f[i-2]
                else:
                    f[i] = 0
            elif int(s[i-2]) == 0 or int(s[i-2]) > 2 or (int(s[i-2]) == 2 and int(s[i-1]) > 6):
                f[i] = f[i-1]
            else:
                f[i] = f[i-1] + f[i-2]
            
        return f[-1]

# @lc code=end

