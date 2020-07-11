#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        s1 = 0
        s2 = -prices[0]

        s3 = max(s1, s2 + prices[1])
        s4 = max(s2, s1 - prices[1])

        for i in range(2, len(prices)):
            t1 = max(s3, s4 + prices[i])
            t2 = max(s4, s1 - prices[i])
            s1 = s3
            s2 = s4
            s3 = t1
            s4 = t2
        
        return s3




        # if len(prices) < 2:
        #     return 0

        # f = [[0 for _ in range(len(prices))] for _ in range(len(prices))]

        # f[0][0] = 0
        # f[0][1] = -prices[0]

        # f[1][0] = max(f[0][0], f[0][1] + prices[1])
        # f[1][1] = max(f[0][1], f[0][0] - prices[1])

        # for i in range(2, len(prices)):
        #     f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
        #     f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i])
        
        # return f[-1][0]

# @lc code=end

