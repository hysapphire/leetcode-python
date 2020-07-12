#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

        # s = 0
        # for _ in range(32):
        #     s = s * 2 + n % 2
        #     n //= 2
        
        # return s
 
# @lc code=end

