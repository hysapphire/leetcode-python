#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        f = [False for _ in range(target + 1)]
        f[0] = True

        for i in range(1, len(nums)):
            if f[target]:
                return True
            for j in range(target, -1, -1):
                if nums[i] <= j:
                    f[j] = f[j] or f[j-nums[i]]
        
        return f[-1]



        # total = sum(nums)
        # if total % 2 == 1:
        #     return False
        # target = total // 2
        # f = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        # for i in range(len(nums)):
        #     f[i][0] = True

        # for i in range(1, len(nums)):
        #     for j in range(target + 1):
        #         if nums[i] <= j:
        #             f[i][j] = f[i-1][j] or f[i-1][j-nums[i]]
            
        #     if f[i][target]:
        #         return True
        
        # return f[-1][-1]

    #     total = sum(nums)
    #     if total % 2 == 1:
    #         return False

    #     return self.dfs(nums, total // 2, total // 2, 0)
    
    # def dfs(self, nums, gap, acc, idx):
    #     if idx == len(nums) or gap < 0 or acc < 0:
    #         return False
    #     if gap == 0:
    #         return True
        
    #     return self.dfs(nums, gap, acc - nums[idx], idx + 1) or self.dfs(nums, gap - nums[idx], acc, idx + 1)

# @lc code=end

