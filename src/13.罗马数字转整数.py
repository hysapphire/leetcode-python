#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        t = len(s) - 1
        num = 0
        for i in range(len(s) - 1, -1, -1):
            if d[s[i]] < d[s[t]]:
                num -= d[s[i]]
            else:
                t = i
                num += d[s[i]]
        
        return num

# @lc code=end

