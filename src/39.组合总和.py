#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        # self.dfs(candidates, target, path, result, 0)
        self.dfs(candidates, target, path, result, target, 0)
        return result

    # def dfs(self, candidates, target, path, result, idx):
    #     s = sum(path)
    #     if s > target:
    #         return
    #     if s == target:
    #         result.append(path[:])
    #         return
    #     for i in range(idx, len(candidates)):
    #         path.append(candidates[i])
    #         self.dfs(candidates, target, path, result, i)
    #         path.pop()
    
    def dfs(self, candidates, target, path, result, gap, idx):
        if gap < 0:
            return
        if gap == 0:
            result.append(path[:])
            return
        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates, target, path, result, gap - candidates[i], i)
            path.pop()

# @lc code=end

