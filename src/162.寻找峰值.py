#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left




        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i+1]:
        #         return i
        
        # return len(nums) - 1


        # nums.insert(0, -float("inf"))
        # nums.append(-float("inf"))
        # for i in range(1, len(nums) - 1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i - 1
        
# @lc code=end

