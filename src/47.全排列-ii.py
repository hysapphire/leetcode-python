#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = []
        path = []
        result = []
        self.dfs(nums, index, path, result)
        return result
    
    def dfs(self, nums, index, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if i in index or (i > 0 and nums[i] == nums[i-1] and i - 1 in index):
                continue
            self.dfs(nums, index + [i],  path + [nums[i]], result)

# @lc code=end

