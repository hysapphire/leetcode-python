#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        max_int = pow(2, 31) - 1
        t = 0
        flag = 1
        i = 0
        while i < len(str) and str[i] == " ":
            i += 1
        
        if i >= len(str):
            return 0

        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            i += 1
            flag = -1
        
        while i < len(str):
            if not str[i].isnumeric():
                break

            if t > max_int // 10 or (t == max_int // 10 and int(str[i])) > max_int % 10:
                return max_int if flag > 0 else -max_int-1
            t = t * 10 + int(str[i])
            i += 1
        
        return flag * t

# @lc code=end

