#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = True

        max_len = 0
        for num in nums:
            if num - 1 not in d:
                t = num
                cnt = 0
                while True:
                    if t in d:
                        cnt += 1
                    else:
                        break
                    t += 1
                max_len = max(max_len, cnt)
        
        return max_len

        # max_len = 0
        # for num in nums:
        #     if d[num]:
        #         d[num] = False
        #         cnt = 1
        #         t = num + 1
        #         while True:
        #             if t in d and d[t]:
        #                 cnt += 1
        #                 d[t] = False
        #             else:
        #                 break
        #             t += 1
        #         t = num - 1
        #         while True:
        #             if t in d and d[t]:
        #                 cnt += 1
        #                 d[t] = False
        #             else:
        #                 break
        #             t -= 1
        #         max_len = max(max_len, cnt)
        
        # return max_len

# @lc code=end

