#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        beginX = 0
        endX = n - 1
        beginY = 0
        endY = n - 1

        cnt = 1
        while True:
            for i in range(beginY, endY + 1):
                matrix[beginX][i] = cnt
                cnt += 1
            beginX += 1
            if beginX > endX:
                break

            for i in range(beginX, endX + 1):
                matrix[i][endY] = cnt
                cnt += 1
            endY -= 1
            if beginY > endY:
                break

            for i in range(endY, beginY - 1, -1):
                matrix[endX][i] = cnt
                cnt += 1
            endX -= 1
            if beginX > endX:
                break

            for i in range(endX, beginX - 1, -1):
                matrix[i][beginY] = cnt
                cnt += 1
            beginY += 1
            if beginY > endY:
                break
    
        return matrix

# @lc code=end

