#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._cnt = 0
        self._max_heapq = []
        self._min_heapq = []

    def addNum(self, num: int) -> None:
        self._cnt += 1
        heapq.heappush(self._max_heapq, (-num, num))
        _, heap_max = heapq.heappop(self._max_heapq)
        heapq.heappush(self._min_heapq, heap_max)
        if self._cnt % 2:
            heap_min = heapq.heappop(self._min_heapq)
            heapq.heappush(self._max_heapq, (-heap_min, heap_min))

    def findMedian(self) -> float:
        if self._cnt % 2:
            return self._max_heapq[0][1]
        else:
            return (self._max_heapq[0][1] + self._min_heapq[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

