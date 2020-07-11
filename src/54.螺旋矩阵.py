#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        result = []
        xs = 0
        xe = n - 1
        ys = 0
        ye = m - 1

        while True:
            for i in range(xs, xe + 1):
                result.append(matrix[ys][i])
            ys += 1
            if ys > ye:
                break

            for i in range(ys, ye + 1):
                result.append(matrix[i][xe])
            xe -= 1
            if xs > xe:
                break

            for i in range(xe, xs-1, -1):
                result.append(matrix[ye][i])
            ye -= 1
            if ys > ye:
                break

            for i in range(ye, ys-1, -1):
                result.append(matrix[i][xs])
            
            xs += 1
            if xs > xe:
                break

        return result

# @lc code=end

