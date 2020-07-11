#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == -1:
            if dividend > -pow(2, 31):
                return -dividend
            else:
                return pow(2, 31) - 1

        flag = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        num = self.div(dividend, divisor)
        
        return num if flag else -num

    def div(self, dividend, divisor):
        if dividend < divisor:
            return 0

        cnt = 1
        s = divisor
        while s + s <= dividend:
            s += s
            cnt += cnt
        
        return cnt + self.div(dividend-s, divisor)

# @lc code=end

