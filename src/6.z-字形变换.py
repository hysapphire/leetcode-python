#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = [[0 for _ in range(len(s))] for _ in range(numRows)] 

        i = 0
        j = 0
        flag = 0
        for ss in s:
            matrix[i][j] = ss
            if flag == 0:
                if i < numRows - 1:
                    i += 1
                else:
                    i -= 1
                    j += 1
                    flag = 1
            elif flag == 1:
                if i > 0:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    flag = 0
        
        res = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    res += matrix[i][j]

        return res

# @lc code=end

