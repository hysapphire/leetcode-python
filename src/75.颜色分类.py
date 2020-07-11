#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        s = 0
        e = len(nums) - 1
        while i <= e:
            if nums[i] == 0:
                t = nums[i]
                nums[i] = nums[s]
                nums[s] = t
                s += 1
                i += 1
            elif nums[i] == 2: 
                t = nums[i]
                nums[i] = nums[e]
                nums[e] = t
                e -= 1
            else:
                i += 1

# @lc code=end

