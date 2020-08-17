#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        m = 0
        sign = 1
        for ss in s:
            if ss == " ":
                continue
            elif ss.isalnum():
                m = m * 10 + int(ss)
            elif ss == "+":
                stack.append(m * sign)
                sign = 1
                m = 0
            elif ss == "-":
                stack.append(m * sign)
                sign = -1
                m = 0
            elif ss == "(":
                if sign == 1:
                    stack.append("(")
                else:
                    stack.append("[")
                sign = 1
            elif ss == ")":
                m = m * sign
                while stack and stack[-1] != "(" and stack[-1] != "[":
                    m += stack.pop()
                if stack.pop() == "[":
                    m = -m
                stack.append(m)
                m = 0

        stack.append(m * sign)
        return sum(stack)

        # stack = []
        # m = 0
        # g = 1
        # for ss in reversed(s):
        #     if ss == " ":
        #         continue
        #     elif ss.isalnum():
        #         m += int(ss) * g
        #         g *= 10
        #     elif ss == "+":
        #         stack.append(m)
        #         m = 0
        #         g = 1
        #     elif ss == "-":
        #         stack.append(-m)
        #         m = 0
        #         g = 1
        #     elif ss == ")":
        #         stack.append(")")
        #     elif ss == "(":
        #         while stack and stack[-1] != ")":
        #             m += stack.pop()
        #         stack.pop()

        #         g = 1

        # stack.append(m)
        # return sum(stack)

# @lc code=end

