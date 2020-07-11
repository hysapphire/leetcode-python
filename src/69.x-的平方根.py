#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x + 1
        while i < j:
            mid = (i + j) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            if tmp > x:
                j = mid
            else:
                i = mid + 1
        
        return i - 1

# @lc code=end

