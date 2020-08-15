#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = list(map(int, version1.split(".")))
        nums2 = list(map(int, version2.split(".")))

        cnt = 0
        for n1, n2 in zip(nums1, nums2):
            cnt += 1
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1

        if len(nums1) < len(nums2):
            for i in range(cnt, len(nums2)):
                if nums2[i] != 0:
                    return -1
            return 0
        elif len(nums1) > len(nums2):
            for i in range(cnt, len(nums1)):
                if nums1[i] != 0:
                    return 1
            return 0
        else:
            return 0

# @lc code=end

