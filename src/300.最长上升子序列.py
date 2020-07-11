#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [1 for _ in range(len(nums))]
        max_len = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
            max_len = max(max_len, f[i])
        
        return max_len
        
# @lc code=end

