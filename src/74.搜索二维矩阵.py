#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        s = 0
        e = row * col

        while s < e:
            mid = s + (e - s) // 2
            r = mid // col
            c = mid % col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] >= target:
                e = mid
            else:
                s = mid + 1
        
        return False

# @lc code=end

