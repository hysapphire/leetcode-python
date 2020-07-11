#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        tmp_sum = 0
        for num in nums:
            if tmp_sum < 0:
                tmp_sum = 0
            tmp_sum += num
            max_sum = max(max_sum, tmp_sum)
        return max_sum

# @lc code=end

