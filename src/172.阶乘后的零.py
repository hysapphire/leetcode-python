#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 0
        while n > 0:
            s += n // 5
            n = n // 5
        
        return s

        # m = 1
        # for i in range(n):
        #     m = m * (i + 1)
        
        # print(m)
        # s = 0
        # while m % 10 == 0:
        #     s += 1
        #     m //= 10
        
        # return s

# @lc code=end

