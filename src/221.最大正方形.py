#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        f = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_edge = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        f[i][j] = 1
                        max_edge = max(max_edge, f[i][j])
                else:
                    if matrix[i][j] == "1":
                        f[i][j] = min(min(f[i-1][j], f[i][j-1]), f[i-1][j-1]) + 1
                        max_edge = max(max_edge, f[i][j])
        
        return max_edge * max_edge

        # if not matrix:
        #     return 0

        # m = len(matrix)
        # n = len(matrix[0])
        # L = [0] * n
        # R = [n] * n
        # H = [0] * n

        # max_area = 0

        # for i in range(m):
        #     left = 0
        #     right = n
        #     for j in range(n):
        #         if matrix[i][j] == "1":
        #             H[j] += 1
        #             L[j] = max(L[j], left)
        #         else:
        #             left = j + 1
        #             H[j] = 0
        #             L[j] = 0
        #             R[j] = n
        #     for j in range(n-1, -1, -1):
        #         if matrix[i][j] == "1":
        #             R[j] = min(R[j], right)
        #             min_edge = min(H[j], R[j] - L[j])
        #             max_area = max(max_area, min_edge * min_edge)
        #         else:
        #             right = j

        # return max_area 

# @lc code=end

