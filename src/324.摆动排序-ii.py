#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]

    #     self.qiuck_select(nums, 0, len(nums), len(nums) // 2)
    #     mid_num = nums[len(nums) // 2]

    #     s = 0
    #     e = len(nums) - 1
    #     i = 0
    #     while i < e:
    #         if nums[i] < mid_num:
    #             t = nums[s]
    #             nums[s] = nums[i]
    #             nums[i] = t
    #             s += 1
    #         elif nums[i] > mid_num:
    #             t = nums[i]
    #             nums[i] = nums[e]
    #             nums[e] = t
    #         i += 1
        
    #     if len(nums) % 2:
    #         mid = len(nums) // 2 + 1
    #     else:
    #         mid = len(nums) // 2

    #     tmp1 = nums[:mid]
    #     tmp2 = nums[mid:]

    #     nums[0::2] = tmp1[::-1]
    #     nums[1::2] = tmp2[::-1]

    # def qiuck_select(self, nums, low, high, n):
    #     pivot = nums[high - 1]
    #     i = low
    #     j = low

    #     while j < high:
    #         if nums[j] <= pivot:
    #             t = nums[i]
    #             nums[i] = nums[j]
    #             nums[j] = t
    #             i += 1
    #         j += 1
    #     if i - 1 > n:
    #         self.qiuck_select(nums, low, i - 1, n)
    #     elif i <= n:
    #         self.qiuck_select(nums, i, high, n)

# @lc code=end

