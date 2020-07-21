#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        result = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result



        # result = []

        # d1 = {}
        # for num in nums1:
        #     d1[num] = d1.get(num, 0) + 1
        
        # d2 = {}
        # for num in nums2:
        #     d2[num] = d2.get(num, 0) + 1
        
        # for num in d1.keys():
        #     n = min(d1[num], d2.get(num, 0))
        #     for _ in range(n):
        #         result.append(num)
        
        # return result

# @lc code=end

