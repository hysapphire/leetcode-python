#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        f = [True] * n
        f[0] = False
        f[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if f[i]:
                j = i * i
                while j < n:
                    f[j] = False
                    j += i
                    
        return f.count(True)

    # def judge(self, n):
    #     if n <= 3:
    #         return True
    #     for i in range(2, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True


    #     count = 0
    #     for i in range(2, n):
    #         if self.judge(i):
    #             count += 1
    #     return count

    # def judge(self, n):
    #     if n <= 3:
    #         return True
    #     for i in range(2, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

# @lc code=end

