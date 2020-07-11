#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            idx = self.partition(nums, low, high)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                low = idx + 1
            else:
                high = idx - 1


    def partition(self, nums, low, high):
        mid = (low + high) // 2
        t = nums[mid]
        nums[mid] = nums[high]
        nums[high] = t
        pivot = nums[high]

        j = low
        for i in range(low, high):
            if nums[i] > pivot:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                j += 1

        t = nums[j]
        nums[j] = nums[high]
        nums[high] = t

        return j

    # def partition(self, nums, low, high):
    #     pivot = nums[high]

    #     j = low
    #     for i in range(low, high):
    #         if nums[i] > pivot:
    #             t = nums[i]
    #             nums[i] = nums[j]
    #             nums[j] = t
    #             j += 1

    #     t = nums[j]
    #     nums[j] = nums[high]
    #     nums[high] = t

    #     return j

# @lc code=end

