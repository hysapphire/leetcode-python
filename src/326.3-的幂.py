#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0
 
        # if n == 0:
        #     return False
        # if n == 1:
        #     return True
        # if n % 3 != 0:
        #     return False
        # return self.isPowerOfThree(n // 3)

# @lc code=end

