#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [0]
        l = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                while stack and nums[i] < nums[stack[-1]]:
                    l = min(l, stack.pop())
            stack.append(i)
        
        stack = [len(nums) - 1]
        r = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    r = max(r, stack.pop())
            stack.append(i)
        
        if r - l > 0:
            return r - l + 1
        else:
            return 0




        # l = len(nums) - 1
        # r = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             l = min(l, i)
        #             r = max(r, j)
        
        # if r - l > 0:
        #     return r - l + 1
        # else:
        #     return 0
        
        
# @lc code=end

