#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = nums[0]
        pos = 0

        while True:
            if max_pos >= len(nums) - 1:
                return True
            if pos > max_pos:
                return False

            max_pos = max(max_pos, nums[pos] + pos)
            pos += 1

# @lc code=end

