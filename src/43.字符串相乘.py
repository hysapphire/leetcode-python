#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        s = "0"
        for i, n in enumerate(reversed(num1)):
            for _ in range(int(n)):
                s = self.add(s, self.multiply_10(num2, i))
        
        return s

    def multiply_10(self, num, n):
        for _ in range(n):
            num += "0"

        return num

    def add(self, num1, num2):
        c = 0
        s = ""
        min_len = min(len(num1), len(num2))

        for i in range(-1, -min_len - 1, -1):
            t = int(num1[i]) + int(num2[i]) + c
            c = t // 10
            t = t % 10
            s = str(t) + s

        num = num1 if len(num1) > len(num2) else num2

        for i in range(-min_len-1, -len(num)-1, -1):
            t = int(num[i]) + c
            c = t // 10
            t = t % 10
            s = str(t) + s

        if c > 0:
            s = str(c) + s

        return s

# @lc code=end

