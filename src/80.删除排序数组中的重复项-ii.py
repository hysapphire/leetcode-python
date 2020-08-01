#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cnt = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt <= 2:
                nums[i] = nums[j]
                i += 1
        
        return i

# @lc code=end

