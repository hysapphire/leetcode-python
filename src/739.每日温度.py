#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(T)
        for i in range(1, len(T)):
            if stack and T[i] > T[stack[-1]]:
                while stack and T[i] > T[stack[-1]]:
                    t = stack.pop()
                    result[t] = i - t
            stack.append(i)
        
        return result
        
# @lc code=end

