#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while (i < j):
            max_area = max(max_area, min(height[j], height[i]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
# @lc code=end

