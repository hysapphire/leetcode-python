#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = numerator * denominator >= 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        n = int(numerator / denominator)
        d = numerator - denominator * n

        str_n = str(n) if flag else "-" + str(n)
        if d == 0:
            return str_n
        s = ""
        cyc = False
        ll = [d]
        while d != 0:
            d *= 10
            s += str(int(d / denominator))
            d = d - int(d / denominator) * denominator
            if d in ll:
                cyc = True
                break
            ll.append(d)

        if not cyc:
            return str_n + "." + s
        else:
            pos = ll.index(d)
            return str_n + "." + s[:pos] + "(" + s[pos:] + ")"

# @lc code=end

