#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax = 1
        fmin = 1
        max_product = nums[0]

        for num in nums:
            a, b = fmax, fmin
            fmax = max(max(a * num, b * num), num)
            fmin = min(min(a * num, b * num), num)
            max_product = max(max_product, fmax)
        
        return max_product

        # fmax = [nums[0]] * len(nums)
        # fmin = [nums[0]] * len(nums)

        # for i in range(1, len(nums)):
        #     fmax[i] = max(max(fmax[i-1] * nums[i], fmin[i-1] * nums[i]), nums[i])
        #     fmin[i] = min(min(fmax[i-1] * nums[i], fmin[i-1] * nums[i]), nums[i])
        
        # return max(fmax)

# @lc code=end

