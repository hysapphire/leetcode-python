#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        t = 2 * total + 1

        if abs(S) > total:
            return 0

        f = [[0 for _ in range(t)] for _ in range(len(nums))]

        f[0][total + nums[0]] = 1
        f[0][total - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(t):
                l = j - nums[i] if j - nums[i] > 0 else 0
                r = j + nums[i] if j + nums[i] < t else 0
                f[i][j] = f[i-1][l] + f[i-1][r]
        
        return f[-1][total + S]



    #     self.sum = 0
    #     self.dfs(nums, 0, S)
    #     return self.sum

    # def dfs(self, nums, idx, diff):
    #     if idx == len(nums):
    #         if diff == 0:
    #             self.sum += 1
    #         return

    #     self.dfs(nums, idx + 1, diff + nums[idx])
    #     self.dfs(nums, idx + 1, diff - nums[idx])
# @lc code=end

