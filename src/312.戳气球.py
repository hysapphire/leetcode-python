#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        f = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for left in range(len(nums)-2, -1, -1):
            for right in range(left + 2, len(nums)):
                for i in range(left+1, right):
                    f[left][right] = max(f[left][right], nums[left] * nums[i] * nums[right] + f[left][i] + f[i][right])

        return f[0][len(nums) - 1]


    #     f = [[None for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)]

    #     nums = [1] + nums + [1]
    #     return self.max_coins(nums, 0, len(nums) - 1, f)

    # def max_coins(self, nums, left, right, f):
    #     if left + 1 == right:
    #         f[left][right] = 0
    #         return 0
    #     if f[left][right] is not None:
    #         return f[left][right]

    #     max_coins = 0
    #     for i in range(left + 1, right):
    #         max_coins = max(max_coins, nums[left] * nums[i] * nums[right] + 
    #         self.max_coins(nums, left, i, f) + self.max_coins(nums, i, right, f))
        
    #     f[left][right] = max_coins
    #     return max_coins
        
# @lc code=end

