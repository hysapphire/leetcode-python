#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        self.dfs(nums, path, result)
        return result
    
    def dfs(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.dfs(nums, path, result)
            path.pop()

# @lc code=end

