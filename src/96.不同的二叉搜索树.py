#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1

        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            for k in range(i):
                f[i] += f[k] * f[i - k - 1]
        
        return f[n]
        
# @lc code=end

