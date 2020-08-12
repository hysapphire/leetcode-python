#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        nums = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                nums[i] = max(nums[i], nums[i-1] + 1)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and nums[i] <= nums[i+1]:
                nums[i] = max(nums[i], nums[i+1] + 1)

        return sum(nums)

# @lc code=end

