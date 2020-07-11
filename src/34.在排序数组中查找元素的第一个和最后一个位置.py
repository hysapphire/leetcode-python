#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left = -1
        # right = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         left = i
        #         break
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == target:
        #         right = i
        #         break
        
        # return [left, right]

        if len(nums) == 0:
            return [-1, -1]

        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        right = j if 0 <= j < len(nums) and nums[j] == target else -1

        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        left = i if 0 <= i < len(nums) and nums[i] == target else -1

        return [left, right]
                
            
# @lc code=end

