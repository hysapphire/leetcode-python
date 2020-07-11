#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        first = root

        while first.left:
            head = first
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next

            first = first.left
        
        return root



        # if not root or not root.left or not root.right:
        #     return root

        # root.left.next = root.right
        # if root.next:
        #     root.right.next = root.next.left
        
        # self.connect(root.left)
        # self.connect(root.right)

        # return root



        # if not root:
        #     return None

        # queue = deque()
        # queue.append(root)
        # dummy = Node(-1)
        # prev = dummy
        # first = root.left
        # while queue:
        #     n = queue.popleft()
        #     if n == first:
        #         prev = dummy
        #         first = n.left

        #     if n.left and n.right:
        #         prev.next = n.left
        #         n.left.next = n.right
        #         prev = n.right
        #         queue.append(n.left)
        #         queue.append(n.right)
        
        # return root



        # if not root:
        #     return None
        # queue1 = deque()
        # queue2 = deque()
        # queue1.append(root)
        # dummy = Node(-1)
        # while queue1:
        #     prev = dummy
        #     while queue1:
        #         n = queue1.popleft()
        #         prev.next = n
        #         prev = n
        #         if n.left:
        #             queue2.append(n.left)
        #         if n.right:
        #             queue2.append(n.right)
        #     queue1 = queue2
        #     queue2 = deque()
        
        # return root
        
# @lc code=end

