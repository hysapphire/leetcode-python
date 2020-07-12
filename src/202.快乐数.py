#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while True:
            if n == 1:
                return True

            if n in d:
                break
            d.add(n)
            t = 0
            while n:
                m = n % 10
                t += m * m
                n //= 10
            n = t
            
        return False

# @lc code=end

