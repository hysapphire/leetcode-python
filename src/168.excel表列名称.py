#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n:
            t = n % 26
            if t == 0:
                t = 26
                n -= 1
            n //= 26
            s = chr(t + ord("A") - 1) + s

        return s
    
# @lc code=end

