#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        L = [0] * n
        R = [n] * n
        H = [0] * n

        max_area = 0

        for i in range(m):
            left = 0
            right = n
            for j in range(n):
                if matrix[i][j] == "1":
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j + 1
                    H[j] = 0
                    L[j] = 0
                    R[j] = n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    R[j] = min(R[j], right)
                    max_area = max(max_area, H[j] * (R[j] - L[j]))
                else:
                    right = j

        return max_area   

# @lc code=end

