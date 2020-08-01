#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ""
        cnt = 0
        for i in range(n):
            t = self.mul(n - i - 1)
            for j in range(n):
                if result.count(str(j+1)) > 0:
                    continue
                if cnt + t < k:
                    cnt += t
                    continue
                result += str(j + 1)
                break
        return result

    def mul(self, x):
        t = 1
        for i in range(1, x + 1):
            t *= i
        return t

    #     path = ""
    #     result = []
    #     self.mm = []
    #     for i in range(n + 1):
    #         self.mm.append(self.mul(i))
    #     self.cnt = 0
    #     self.dfs(n, path, result, k)
    #     return result[0]

    # def mul(self, x):
    #     t = 1
    #     for i in range(1, x + 1):
    #         t *= i
    #     return t

    # def dfs(self, n, path, result, k):
    #     print(self.cnt)
    #     if self.cnt >= k:
    #         return

    #     # t = self.mul(n - len(path))
    #     t = self.mm[n - len(path)]
    #     if self.cnt + t < k:
    #         self.cnt += t
    #         return

    #     if len(path) == n:
    #         result.append(path[:])
    #         return

    #     for i in range(1, n + 1):
    #         if path.count(str(i)) > 0:
    #             continue
    #         self.dfs(n, path + str(i), result, k)

# @lc code=end

