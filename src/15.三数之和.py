#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num_dict = {}
            set_b = {}
            target = -num
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in set_b or nums[j] in set_b:
                    continue
                if diff not in num_dict:
                    num_dict[nums[j]] = j
                else:
                    result.append([num, diff, nums[j]])
                    set_b[nums[j]] = j 
        return result

# @lc code=end

