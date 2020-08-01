#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        self.dfs(n, k, path, result, 1)
        return result

    def dfs(self, n, k, path, result, idx):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(idx, n + 1):
            if i in path:
                continue
            self.dfs(n, k, path + [i], result, i + 1)

# @lc code=end

