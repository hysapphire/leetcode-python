#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        s = newInterval[0]
        e = newInterval[1]
        flag = False
        for interval in intervals:
            if flag:
                res.append(interval)
                continue

            if s > interval[1]:
                res.append(interval)
            else:
                s = min(s, interval[0])
            if e < interval[0]:
                res.append([s, e])
                res.append(interval)
                flag = True
            else:
                e = max(e, interval[1])
        
        if e >= intervals[-1][1]:
            res.append([s, e])
        
        return res

# @lc code=end

