#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = -1
        swap = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos = i
                break
        
        if pos == -1:
            return nums.sort()
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[pos - 1]:
                swap = i
                break
        
        t = nums[swap]
        nums[swap] = nums[pos - 1]
        nums[pos - 1] = t
        nums[pos:] = sorted(nums[pos:])
        return nums
            

# @lc code=end