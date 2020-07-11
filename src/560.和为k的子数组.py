#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        s = 0
        cnt = 0

        for i in range(len(nums)):
            s += nums[i]
            if s - k in d:
                cnt += d[s-k]
            d[s] = d.get(s, 0) + 1
        
        return cnt




        # f = [0] * (len(nums) + 1)

        # for i in range(1, len(nums) + 1):
        #     f[i] = f[i-1] + nums[i-1]
        
        # cnt = 0
        # for i in range(len(nums) + 1):
        #     for j in range(i+1, len(nums) + 1):
        #         if f[j] - f[i] == k:
        #             cnt += 1
        
        # return cnt

# @lc code=end

