#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                j += 1



        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         j += 1
                        
        # while j < len(nums):
        #     nums[j] = 0
        #     j += 1


        # i = 0
        # j = 0
        # while i < len(nums) and j < len(nums):
        #     while i < len(nums) and nums[i] != 0:
        #         i += 1
        #     while j < len(nums) and nums[j] == 0:
        #         j += 1
        #     if i < len(nums) and j < len(nums) and i < j:
        #         nums[i] = nums[j]
        #         nums[j] = 0
        #     else:
        #         j += 1

# @lc code=end

