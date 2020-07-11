#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        result = [[1]]
        for i in range(1, numRows):
            res = []
            res.append(1)
            for j in range(1, len(result[i-1])):
                res.append(result[i-1][j] + result[i-1][j-1])
            res.append(1)
            result.append(res)
        
        return result

# @lc code=end

