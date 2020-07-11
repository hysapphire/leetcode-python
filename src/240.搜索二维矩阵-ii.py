#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        
        return False

    #     if not matrix:
    #         return False
    #     searched = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    #     return self.search_matrix(matrix, len(matrix), len(matrix[0]), 0, 0, target, searched)
    
    # def search_matrix(self, matrix, m, n, i, j, target, searched):
    #     if i < 0 or j < 0 or i >=m or j >= n:
    #         return False

    #     if searched[i][j]:
    #         return False

    #     if matrix[i][j] == target:
    #         searched[i][j] = True
    #         return True
        
    #     if matrix[i][j] > target:
    #         searched[i][j] = True
    #         return False
        
    #     return self.search_matrix(matrix, m, n, i + 1, j, target, searched) \
    #         or self.search_matrix(matrix, m, n, i, j + 1, target, searched)

# @lc code=end

