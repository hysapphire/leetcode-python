#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0 for _ in range(len(obstacleGrid[0]))]
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j-1]
        
        return dp[-1]

        # dp = [1 for _ in range(len(obstacleGrid[0]))]

        # for i in range(len(obstacleGrid)):
        #     for j in range(len(obstacleGrid[0])):
        #         if obstacleGrid[i][j] == 1:
        #             dp[j] = 0
        #         else:
        #             if i > 0 and j > 0:
        #                 dp[j] = dp[j] + dp[j-1]
        #             elif j > 0:
        #                 dp[j] = dp[j-1]
        
        # return dp[-1]

# @lc code=end

