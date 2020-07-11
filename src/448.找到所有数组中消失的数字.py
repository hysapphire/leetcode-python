#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        result = [i + 1 for i, n in enumerate(nums) if n > 0]

        return result




        # for i in range(len(nums)):
        #     idx = (nums[i] - 1) % len(nums)
        #     nums[idx] += len(nums)

        # result = [i + 1 for i, n in enumerate(nums) if n <= len(nums)]

        # return result 


        # for i in range(len(nums)):
        #     while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
        #         t = nums[nums[i] - 1]
        #         nums[nums[i] - 1] = nums[i]
        #         nums[i] = t
        
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] != i + 1:
        #         result.append(i + 1)
        
        # return result
        
# @lc code=end

