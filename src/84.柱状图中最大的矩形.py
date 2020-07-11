#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max_area = 0
        # for mid in range(len(heights)):
        #     left = mid
        #     right = mid
        #     while left >= 0 and heights[left] >= heights[mid]:
        #         left -= 1
            
        #     while right <= len(heights) - 1 and heights[right] >= heights[mid]:
        #         right += 1
            
        #     max_area = max(max_area, heights[mid] * (right - left - 1))
        
        # return max_area

        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    tmp = stack.pop()
                    if not stack:
                        max_area = max(max_area, heights[tmp] * i)
                    else:
                        max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
                stack.append(i)
        
        return max_area

# @lc code=end

