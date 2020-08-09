#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        f = [0]
        for row in triangle:
            for i in range(len(row) - 1, -1, -1):
                if i == 0:
                    f[i] += row[0]
                elif i == len(row) - 1:
                    f.append(f[-1] + row[i])
                else:
                    f[i] = min(f[i-1], f[i]) + row[i]

        return min(f)

# @lc code=end

