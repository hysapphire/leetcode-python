#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
    #     if not root or not (root.left or root.right):
    #         return root
        
    #     if root.left and root.right:
    #         root.left.next = root.right
    #         root.right.next = self.get_next_child(root.next)
    #     elif root.left:
    #         root.left.next = self.get_next_child(root.next)
    #     elif root.right:
    #         root.right.next = self.get_next_child(root.next)

    #     self.connect(root.right)
    #     self.connect(root.left)

    #     return root


    # def get_next_child(self, root):
    #     while root and not (root.left or root.right):
    #         root = root.next
    #     if root:
    #         if root.left:
    #             return root.left
    #         else:
    #             return root.right
        
    #     return None



        from collections import deque

        if not root:
            return root
        
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i > 0:
                    prev.next = node
                prev = node

        return root



        # if not root:
        #     return root
        
        # cur = [root]
        # nex = []
        # prev = None
        # while True:
        #     if not cur:
        #         break

        #     for n in cur:
        #         if n.left:
        #             nex.append(n.left)
        #         if n.right:
        #             nex.append(n.right)
        #         if prev:
        #             prev.next = n
                
        #         prev = n
            
        #     prev = None
        #     cur = nex
        #     nex = []

        # return root
        
# @lc code=end

