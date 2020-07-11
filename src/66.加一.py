#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            c = digits[i] // 10
            digits[i] %= 10
        
        if c == 1:
            digits.insert(0, 1)

        return digits
# @lc code=end

