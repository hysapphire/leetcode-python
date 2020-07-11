#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
from itertools import cycle
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = 0
        run = 0
        start = 0
        for i in range(len(gas)):
            run += gas[i] - cost[i]
            rest += gas[i] - cost[i]
            if run < 0:
                run = 0
                start = i + 1
        
        return start if rest >= 0 else -1
            
# @lc code=end

