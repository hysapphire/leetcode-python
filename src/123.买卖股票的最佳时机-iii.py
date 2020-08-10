#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # f[i][1][0] = max(f[i-1][1][0], f[i-1][1][1] + prices[i])
        # f[i][1][1] = max(f[i-1][1][1], - prices[i])
        # f[i][2][0] = max(f[i-1][2][0], f[i-1][2][1] + prices[i])
        # f[i][2][1] = max(f[i-1][2][1], f[i-1][1][0] - prices[i])

        f_i10 = 0
        f_i11 = -float("inf")
        f_i20 = 0
        f_i21 = -float("inf")
        for price in prices:
            f_i20 = max(f_i20, f_i21 + price)
            f_i21 = max(f_i21, f_i10 - price)
            f_i10 = max(f_i10, f_i11 + price)
            f_i11 = max(f_i11, -price)
        
        return f_i20



        # if not prices:
        #     return 0

        # f = [[[0, 0] for _ in range(3)] for _ in range(len(prices))]

        # for i in range(len(prices)):
        #     for k in range(1, 3):
        #         if i == 0:
        #             f[i][k][0] = 0
        #             f[i][k][1] = -prices[i]
        #             continue
        #         f[i][k][0] = max(f[i-1][k][0], f[i-1][k][1] + prices[i])
        #         f[i][k][1] = max(f[i-1][k][1], f[i-1][k-1][0] - prices[i])

        # return f[-1][-1][0]

# @lc code=end

