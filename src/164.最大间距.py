#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_value = max(nums)
        ranked = [0] * len(nums)
        exp = 1

        while max_value // exp > 0:
            count = [0] * 10
            for n in nums:
                count[n // exp % 10] += 1
            
            for i in range(1, len(count)):
                count[i] += count[i - 1]

            for i in range(len(ranked) - 1, -1, -1):
                count[nums[i] // exp % 10] -= 1
                ranked[count[nums[i] // exp % 10]] = nums[i]
            
            nums = ranked[:]
            exp *= 10
        
        max_gap = -float("inf")
        for i in range(len(ranked) - 1):
            max_gap = max(max_gap, ranked[i + 1] - ranked[i])
        
        return max_gap

# @lc code=end

