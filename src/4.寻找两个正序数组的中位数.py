#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        total_len =  len_nums1 + len_nums2

        flag = total_len % 2 == 1
        idx = total_len // 2 + total_len % 2

        i = 0
        j = 0
        k = 1
        median = 0

        while i < len_nums1 or j < len_nums2:
            if i < len_nums1 and j < len_nums2:
                if nums1[i] < nums2[j]:
                    num = nums1[i]
                    i += 1
                else:
                    num = nums2[j]
                    j += 1
            elif i < len_nums1:
                num = nums1[i]
                i += 1
            else:
                num = nums2[j]
                j += 1

            if flag and k == idx:
                return num
            elif not flag and k == idx:
                median += num
            elif not flag and k == idx + 1:
                median += num
                return median / 2

            k += 1
                  

# @lc code=end

