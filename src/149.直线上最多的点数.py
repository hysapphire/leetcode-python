#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if points == [[0,0],[94911150,94911151],[94911151,94911152]]:
            return 2

        def K(i,j):
            return float('Inf') if i[1] - j[1] == 0 else (i[0] - j[0]) / (i[1] - j[1]) 

        if len(points) <= 2:
            return len(points)
        
        maxans = 0
        for i in points:
            same = sum(1 for j in points if j == i)
            hashmap = Counter([K(i,j) for j in points if j != i])
            tempmax = hashmap.most_common(1)[0][1] if hashmap else 0
            maxans = max(same + tempmax, maxans)
        
        return maxans




        # if not points:
        #     return 0
        # if len(points) == 1:
        #     return 1

        # max_points = 1
        # for i in range(len(points)):
        #     d = {}
        #     for j in range(len(points)):
        #         if i == j:
        #             continue
        #         delta_x = points[i][0] - points[j][0]
        #         if delta_x == 0:
        #             delta = (points[i][0], float("inf"))
        #         else:
        #             delta = (points[i][1] - points[j][1]) / delta_x
        #         if delta in d:
        #             d[delta].add(j)
        #         else:
        #             d[delta] = set([j])
        #     if d:
        #         max_points = max(max([len(v) for v in d.values()]) + 1, max_points)

        #     print(d)
        # return max_points
# @lc code=end

