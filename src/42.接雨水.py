#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        tmp_max = 0
        for i in range(len(height)):
            tmp_max = max(tmp_max, height[i])
            left_max[i] = tmp_max
        
        tmp_max = 0
        for i in range(len(height) - 1, -1, -1):
            tmp_max = max(tmp_max, height[i])
            right_max[i] = tmp_max
        
        total = 0
        for i in range(len(height)):
            total += min(left_max[i], right_max[i]) - height[i]
        
        return total

# @lc code=end

