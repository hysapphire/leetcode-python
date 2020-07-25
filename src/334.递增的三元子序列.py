#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        r1 = float("inf")
        r2 = float("inf")
        for n in nums:
            if n <= r1:
                r1 = n
            elif n <= r2:
                r2 = n
            else:
                return True
        
        return False
        
# @lc code=end

