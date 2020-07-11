#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += (prices[i] - prices[i-1] if prices[i] - prices[i-1] > 0 else 0)
        
        return max_profit
        
# @lc code=end

