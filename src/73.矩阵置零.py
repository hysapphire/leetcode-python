#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = False
        col = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if row:
            for j in range(n):
                matrix[0][j] = 0
        
        if col:
            for i in range(m):
                matrix[i][0] = 0

        # m = len(matrix)
        # n = len(matrix[0])
        # row = 0
        # col = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row |= 1 << i
        #             col |= 1 << j

        # cnt = 0
        # while row != 0:
        #     r = row % 2
        #     row >>= 1
        #     if r:
        #         for i in range(n):
        #             matrix[cnt][i] = 0
        #     cnt += 1

        # cnt = 0
        # while col != 0:
        #     c = col % 2
        #     col >>= 1
        #     if c:
        #         for i in range(m):
        #             matrix[i][cnt] = 0
        #     cnt += 1

# @lc code=end

