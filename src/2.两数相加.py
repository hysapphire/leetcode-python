#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        c = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + c
            c = s // 10
            n = s % 10
            node.next = ListNode(n)
            node = node.next

            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        
        if c > 0:
            node.next = ListNode(c)
        
        return dummy.next

# @lc code=end

