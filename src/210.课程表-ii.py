#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adjacency[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            p = queue.pop(0)
            numCourses -= 1
            result.append(p)
            for pp in adjacency[p]:
                indegree[pp] -= 1
                if indegree[pp] == 0:
                    queue.append(pp)
        
        if numCourses != 0:
            return []
        
        return result

# @lc code=end

