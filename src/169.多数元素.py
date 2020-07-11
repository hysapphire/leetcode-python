#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if majority_element == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    majority_element = nums[i]
                    cnt = 1

        return majority_element

# @lc code=end

