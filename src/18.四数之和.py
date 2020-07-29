#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        d = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                s = j + 1
                e = len(nums) - 1
                while s < e:
                    ss = nums[i] + nums[j] + nums[s] + nums[e]
                    if ss < target:
                        s += 1
                    elif ss > target:
                        e -= 1
                    else:
                        d.append([nums[i], nums[j], nums[s], nums[e]])
                        while s < e and nums[s] == nums[s+1]:
                            s += 1
                        while s < e and nums[e] == nums[e-1]:
                            e -= 1
                        
                        s += 1
                        e -= 1
        
        return d

        # nums.sort()
        # d = set()
        # for i in range(len(nums) - 3):
        #     for j in range(i + 1, len(nums) - 2):
        #         s = j + 1
        #         e = len(nums) - 1
        #         while s < e:
        #             ss = nums[i] + nums[j] + nums[s] + nums[e]
        #             if ss < target:
        #                 s += 1
        #             elif ss > target:
        #                 e -= 1
        #             else:
        #                 d.add((nums[i], nums[j], nums[s], nums[e]))
        #                 s += 1
        #                 e -= 1
        
        # return list(d)

# @lc code=end

