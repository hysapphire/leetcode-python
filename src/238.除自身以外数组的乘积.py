#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]

        return result

        # left = [1] * len(nums)
        # right = [1] * len(nums)
        # result = []

        # for i in range(1, len(nums)):
        #     left[i] = left[i - 1] * nums[i - 1]
        # for i in range(len(nums) - 2, -1, -1):
        #     right[i] = right[i + 1] * nums[i + 1]
        
        # for i in range(len(nums)):
        #     result.append(left[i] * right[i])
        
        # return result
# @lc code=end

