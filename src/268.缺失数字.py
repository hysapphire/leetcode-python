#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums):
                t = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = t
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)

# @lc code=end

