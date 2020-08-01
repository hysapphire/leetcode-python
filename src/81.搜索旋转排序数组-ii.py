#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (j + i) // 2
            if nums[mid] == target:
                return True
        
            if nums[i] < nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[i] > nums[mid]:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                i += 1
            
        return False
            
# @lc code=end

