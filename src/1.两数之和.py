#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from collections import defaultdict
from typing import List
# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         num_dict = defaultdict(list)
#         for idx, num in enumerate(nums):
#             num_dict[num].append(idx)
        
#         for key, values in num_dict.items():
#             diff = target - key
#             if num_dict.get(diff, None) is not None:
#                 for i in values:
#                     for j in num_dict[diff]:
#                         if i == j:
#                             continue
#                         result.append(i)
#                         result.append(j)
#                         return result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], idx]
            else:
                num_dict[num] = idx


# @lc code=end