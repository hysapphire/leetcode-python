#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        f = [0] * len(nums)
        f[0] = nums[0]
        f[1] = max(f[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i-2] + nums[i], f[i - 1])
        
        return f[-1]
# @lc code=end

