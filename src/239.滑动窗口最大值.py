#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            if queue and i - queue[0] + 1 > k:
                queue.popleft()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


        # return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
# @lc code=end

