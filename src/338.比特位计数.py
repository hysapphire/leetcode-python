#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)

        for i in range(1, num + 1):
            result[i] = result[i & (i-1)] + 1

        return result


        # if num == 0:
        #     return [0]
        # if num == 1:
        #     return [0, 1]

        # result = [1] * (num + 1)
        # result[0] = 0

        # tmp = 1
        # for i in range(2, num + 1):
        #     if i == tmp * 2:
        #         tmp *= 2
        #         continue
        #     result[i] = result[i - tmp] + 1

        # return result
        
# @lc code=end

