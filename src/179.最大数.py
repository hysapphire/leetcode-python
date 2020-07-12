#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=LargerNumKey)
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
        

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x



    #     if all([n == 0 for n in nums]):
    #         return "0"
    #     nums = [str(n) for n in nums]
    #     self.sort(nums)
        
    #     return "".join(nums)

    # def compare(self, a, b):
    #     len_a = len(a)
    #     len_b = len(b)
    #     for i in range(min(len_a, len_b)):
    #         if a[i] < b[i]:
    #             return True
    #         elif a[i] > b[i]:
    #             return False

    #     if len_a < len_b:
    #         return self.compare(a, b[len_a - len_b:])
    #     elif len_a > len_b:
    #         return self.compare(a[len_b - len_a:], b)
    #     return False

    # def sort(self, nums):
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             if self.compare(nums[i], nums[j]):
    #                 t = nums[i]
    #                 nums[i] = nums[j]
    #                 nums[j] = t

# @lc code=end

