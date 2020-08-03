#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        size = 1 << n
        for i in range(size):
            res.append(i ^ i // 2)
        
        return res

# @lc code=end

