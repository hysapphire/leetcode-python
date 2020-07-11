#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            
            flags[i] = 1

            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adjacency[prerequisite[1]].append(prerequisite[0])
        
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False

        return True



        # indegree = [0 for _ in range(numCourses)]
        # adjacency = [[] for _ in range(numCourses)]

        # for prerequisite in prerequisites:
        #     adjacency[prerequisite[1]].append(prerequisite[0])
        #     indegree[prerequisite[0]] += 1
        
        # queue = deque()

        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        
        # while queue:
        #     pre = queue.popleft()
        #     numCourses -= 1
        #     for cur in adjacency[pre]:
        #         indegree[cur] -= 1
        #         if indegree[cur] == 0:
        #             queue.append(cur)
        
        # return not numCourses




        # d = {}
        # for prerequisite in prerequisites:
        #     d[prerequisite[0]] = prerequisite[1]
        
        # for prerequisite in prerequisites:
        #     f = {prerequisite[0]}
        #     tmp = prerequisite[1]
        #     while tmp not in f and tmp in d:
        #         f.add(tmp)
        #         tmp = d[tmp]

        #     if tmp == prerequisite[0]:
        #         return False
        
        # return True
# @lc code=end

