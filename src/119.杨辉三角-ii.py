#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]
        for _ in range(rowIndex):
            for i in range(len(nums) - 1):
                nums[i] = nums[i] + nums[i+1]
            nums = [1] + nums

        return nums
# @lc code=end

