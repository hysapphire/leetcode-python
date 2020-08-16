#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        if k > len(prices) // 2:
            return self.max_profit(prices)

        f = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]

        for i in range(k + 1):
            f[0][i][0] = 0
            f[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k + 1):
                if j == 0:
                    f[i][j][0] = 0
                    f[i][j][1] = -float("inf")
                else:    
                    f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + prices[i])
                    f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - prices[i])

        return f[-1][-1][0]
    
    def max_profit(self, prices):
        s = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                s += prices[i] - prices[i-1]
        
        return s
 
# @lc code=end

