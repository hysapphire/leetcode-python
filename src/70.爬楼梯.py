#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        p = 0
        q = 1
        r = p + q
        for _ in range(1, n):
            p = q
            q = r
            r = p + q

        return r
 
# @lc code=end

