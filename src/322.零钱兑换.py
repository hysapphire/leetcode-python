#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float("inf")] * (amount + 1)
        f[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] = min(f[i], f[i-coin] + 1)

        return -1 if f[-1] == float("inf") else f[-1]



        # f = [float("inf")] * (amount + 1)
        # f[0] = 0
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if i - coin < 0 or f[i-coin] == float("inf"):
        #             continue
        #         f[i] = min(f[i], f[i-coin] + 1)

        # return -1 if f[-1] == float("inf") else f[-1]



        # self.min_num = float("inf")

        # def dfs(coins, num, diff):
        #     if diff < 0:
        #         return
        #     if diff == 0:
        #         self.min_num = min(self.min_num, num)
        #         return
            
        #     for coin in coins:
        #         dfs(coins, num + 1, diff - coin)
        
        # dfs(coins, 0, amount)
        # return -1 if self.min_num == float("inf") else self.min_num

# @lc code=end

