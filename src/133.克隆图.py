#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}

        def dfs(node):
            if not node:
                return 
            if node in d:
                return d[node]
            n = Node(node.val)
            d[node] = n
            for neighbor in node.neighbors:
                n.neighbors.append(dfs(neighbor))
            
            return n
        
        return dfs(node)


        # if not node:
        #     return None
        
        # first = Node(node.val)
        # q = deque([node])
        # d = {node: first}
        # while q:
        #     n = q.popleft()

        #     for neighbor in n.neighbors:
        #         if neighbor not in d:
        #             d[neighbor] = Node(neighbor.val)
        #             q.append(neighbor)
        #         d[n].neighbors.append(d[neighbor])

        # return first
        
# @lc code=end

