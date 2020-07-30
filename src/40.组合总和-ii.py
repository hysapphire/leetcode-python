#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        self.dfs(candidates, path, result, 0, target)
        return result
    
    def dfs(self, candidates, path, result, idx, gap):
        if gap < 0:
            return
        if gap == 0:
            result.append(path[:])
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, path + [candidates[i]], result, i+1, gap - candidates[i])
        
# @lc code=end

