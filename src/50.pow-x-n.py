#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = 1
        i = abs(n)
        while i != 0:
            if i % 2:
                m *= x
            x *= x
            i //= 2
        
        return m if n > 0 else 1 / m

    #     if n == 0:
    #         return 1
    #     if x == 0:
    #         return 0

    #     flag = n > 0
    #     n = abs(n)
        
    #     d = {}
    #     m = self.my_pow(x, n, d)
    #     if flag:
    #         return m
    #     else:
    #         return 1 / m

    # def my_pow(self, x, n, d):
    #     if n in d:
    #         return d[n]
    #     if n == 0:
    #         d[0] = 1
    #         return 1
    #     if n == 1:
    #         d[1] = x
    #         return x
        
    #     m = self.my_pow(x, n // 2, d) * self.my_pow(x, n - n // 2, d)
    #     d[n] = m
    #     return m

# @lc code=end

