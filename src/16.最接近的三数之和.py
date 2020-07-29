#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        min_diff = float("inf")
        min_diff_sum = 0

        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                cur_sum = nums[i] + nums[s] + nums[e]
                if abs(cur_sum - target) < min_diff:
                    min_diff = abs(cur_sum - target)
                    min_diff_sum = cur_sum
        
                if cur_sum > target:
                    e -= 1
                elif cur_sum < target:
                    s += 1
                else:
                    return target
        
        return min_diff_sum

# @lc code=end

