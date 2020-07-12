#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

        return nums



        # k = k % len(nums)
        # count = 0
        # for i in range(len(nums)):
        #     curr = i
        #     t = nums[i]
        #     while True:
        #         j = (curr + k) % len(nums)
        
        #         m = nums[j]
        #         nums[j] = t
        #         t = m
        #         curr = j
        #         count += 1
        #         if curr == i:
        #             break
        #     if count >= len(nums):
        #         break




        # k = k % len(nums)
        # count = 0
        # for i in range(len(nums)):
        #     curr = i
        #     prev = nums[i]

        #     while True:
        #         p = (curr + k) % len(nums)
        #         tmp = nums[p]
        #         nums[p] = prev
        #         prev = tmp
        #         curr = p
        #         count += 1
        #         if i == curr:
        #             break

        #     if count >= len(nums):
        #         break
                


        # for _ in range(k):
        #     prev = nums[-1]
        #     for i in range(len(nums)):
        #         tmp = nums[i]
        #         nums[i] = prev
        #         prev = tmp


# @lc code=end

