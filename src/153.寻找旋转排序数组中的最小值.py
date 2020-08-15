#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums) - 1

        while begin < end:
            mid = (begin + end) // 2

            if nums[mid] > nums[end]:
                begin = mid + 1
            else:
                end = mid
        
        return nums[begin]


        # begin = 0
        # end = len(nums) - 1

        # while begin < end:
        #     mid = (begin + end) // 2

        #     if nums[begin] < nums[end]:
        #         end = mid
        #     else:
        #         if nums[mid] > nums[begin]:
        #             begin = mid
        #         elif nums[mid] < nums[begin]:
        #             end = mid
        #         else:
        #             begin = mid + 1

        # return nums[begin]

# @lc code=end

