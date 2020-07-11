#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [r + [num] for r in result]
        
        return result

    #     result = []
    #     path = []
    #     self.dfs(nums, path, 0, result)
    #     return result

    # def dfs(self, nums, path, idx, result):
    #     if idx == len(nums):
    #         result.append(path[:])
    #         return
        
    #     path.append(nums[idx])
    #     self.dfs(nums, path, idx + 1, result)
    #     path.pop()
    #     self.dfs(nums, path, idx + 1, result)

    #     return result

    #     result = []
    #     path = []
    #     self.dfs(nums, path, 0, result)
    #     return result
    
    # def dfs(self, nums, path, idx, result):
    #     result.append(path[:])

    #     for i in range(idx, len(nums)):
    #         path.append(nums[i])
    #         self.dfs(nums, path, i + 1, result)
    #         path.pop()
        
    #     return result

# @lc code=end

