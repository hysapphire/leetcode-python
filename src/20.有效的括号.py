#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        str_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for ss in s:
            if ss in ["(", "{", "["]:
                stack.append(ss)
            else:
                if len(stack) > 0 and str_map[ss] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
# @lc code=end
