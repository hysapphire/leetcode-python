#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + t + b))))

        return int(stack[-1])


        # stack = []
        # for t in tokens:
        #     if t != "+" and t != "-" and t != "*" and t != "/":
        #         stack.append(int(t))
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()
        #         if t == "+":
        #             c = a + b
        #         elif t == "-":
        #             c = a - b
        #         elif t == "*":
        #             c = a * b
        #         else:
        #             c = int(a / b)
        #         stack.append(c)

        # return stack[-1]

# @lc code=end

