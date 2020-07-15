#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
import heapq
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        points = []
        heap = [[0, float('inf')]]
        res = [[0, 0]]

        #1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r)) #这里负号将最小堆，变成了最大堆
            points.append((r, h, 0)) #r的右端点为0

        #2.将端点从小到大排序
        points.sort() #如果当前点相等，则按照高度升序

        #3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:
            while l >= heap[0][1]: #出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
                heapq.heappop(heap)
            if h < 0: #入堆：所有左端点都要入堆
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]: #关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
        return res[1:]


        # if not buildings:
        #     return []
        # x = []
        # for building in buildings:
        #     x.append(building[0])
        #     x.append(building[1])
        # x.sort()

        # result = []
        # y = []
        # for i in range(1, len(x)):
        #     x0 = x[i-1]
        #     x1 = x[i]
        #     max_y = 0
        #     for building in buildings:
        #         if building[0] > x1:
        #             break
        #         if building[0] <= x0 and building[1] >= x1:
        #             max_y = max(max_y, building[2])
        #     if not y or max_y != y[-1]:
        #         result.append([x[i-1], max_y])
        #     y.append(max_y)
        
        # result.append([x[-1], 0])


        # # x.append(float("inf"))
        # # y.append(0)

        # # result = []
        # # result.append([x[0], y[0]])
        # # for i in range(1, len(y)):
        # #     if y[i] == y[i-1]:
        # #         continue
        # #     else:
        # #         result.append([x[i], y[i]])

        # # xx = []
        # # yy = []
        # # xx0 = x[0]
        # # xx1 = x[1]
        # # for i in range(1, len(y)):
        # #     if y[i] == y[i-1]:
        # #         xx0 = min(xx0, x[i])
        # #         xx1 = max(xx1, x[i+1])
        # #     else:
        # #         xx.append([xx0, xx1])
        # #         yy.append(y[i-1])
        # #         xx0 = x[i]
        # #         xx1 = x[i + 1]
        
        # # xx.append([xx0, xx1])
        # # yy.append(y[-1])
        # # result = []
        # # for xxx, yyy in zip(xx, yy):
        # #     result.append([xxx[0], yyy])
        
        # return result

# @lc code=end

