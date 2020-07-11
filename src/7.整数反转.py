#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        max_int = (pow(2, 31) - 1) // 10
        min_int = pow(2, 31) // 10
        flag = -1 if x < 0 else 1
        t = 0
        x = abs(x)
        while x != 0:
            print(t)
            if (flag > 0 and t > max_int) or (flag < 0 and t > min_int):
                return 0
            t = t * 10 + x % 10
            x = x // 10

        return flag * t

        # flag = -1 if x < 0 else 1
        # t = 0
        # x = abs(x)
        # while x > 0:
        #     t = t * 10 + x % 10
        #     x = x // 10
        # if flag == 1:
        #     if t > pow(2, 31) - 1:
        #         return 0
        #     else:
        #         return t
        # else:
        #     if t > pow(2, 31):
        #         return 0
        #     else:
        #         return -t

# @lc code=end

