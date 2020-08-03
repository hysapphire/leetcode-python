#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        self.dfs(nums, path, result, 0)
        return result
    
    def dfs(self, nums, path, result, idx):
        result.append(path[:])

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            if not path:
                if i > 0 and nums[i] == nums[i-1]:
                    continue

            self.dfs(nums, path + [nums[i]], result, i+1)

# @lc code=end

