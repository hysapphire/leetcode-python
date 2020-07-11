#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        node1 = head
        node2 = dummy
        d = {}
        while node1:
            node2.next = Node(node1.val)
            d[node1] = node2.next
            node1 = node1.next
            node2 = node2.next
        
        node1 = head
        node2 = dummy.next
        while node1 and node2:
            if node1.random:
                node2.random = d[node1.random]
            
            node1 = node1.next
            node2 = node2.next
        
        return dummy.next



        # node = head
        # while node:
        #     next_node = node.next
        #     node.next = Node(node.val)
        #     node.next.next = next_node
        #     node = next_node
        
        # node = head
        # while node:
        #     if node.random:
        #         node.next.random = node.random.next
        #     node = node.next.next
        
        # dummy = Node(-1)
        # node1 = head
        # node2 = dummy

        # while node1:
        #     node2.next = node1.next
        #     node2 = node2.next
        #     node1.next = node1.next.next
        #     node1 = node1.next
        
        # return dummy.next
        
# @lc code=end

