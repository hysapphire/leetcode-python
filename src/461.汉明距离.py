#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n =  x ^ y
        
        cnt = 0
        while n != 0:
            n &= (n - 1)
            cnt += 1
        
        return cnt
        
# @lc code=end

