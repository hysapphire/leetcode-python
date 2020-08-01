#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        min_len = min(len(a), len(b))
        s = ""
        for i in range(-1, -min_len-1, -1):
            t = int(a[i]) + int(b[i]) + c
            c = t // 2
            t = t % 2
            s = str(t) + s
        
        n = a if len(a) > min_len else b
        for i in range(-min_len-1, -len(n)-1, -1):
            t = int(n[i]) + c
            c = t // 2
            t = t % 2
            s = str(t) + s
        
        if c > 0:
            s = str(c) + s
        
        return s
        
# @lc code=end

