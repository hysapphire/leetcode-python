#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left



        # n = len(matrix)
        # hq = [(matrix[i][0], i, 0) for i in range(n)]
        # heapq.heapify(hq)

        # for _ in range(k - 1):
        #     _, x, y = heapq.heappop(hq)
        #     if y < n - 1:
        #         heapq.heappush(hq, (matrix[x][y+1], x, y + 1))
        
        # return heapq.heappop(hq)[0]
        
# @lc code=end

