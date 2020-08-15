#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                break
            elif s > target:
                j -= 1
            else:
                i += 1
        
        return [i + 1, j + 1]

# @lc code=end

