#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while i != nums[i] - 1:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = t

# @lc code=end

