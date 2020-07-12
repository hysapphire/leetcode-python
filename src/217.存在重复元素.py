#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


        # if not nums:
        #     return False

        # d = set()
        # for num in nums:
        #     if num in d:
        #         return True
        #     else:
        #         d.add(num)
        
        # return False

# @lc code=end

