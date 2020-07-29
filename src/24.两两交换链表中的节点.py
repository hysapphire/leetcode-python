#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node and node.next and node.next.next:
            tmp = node.next.next.next
            tmp2 = node.next
            node.next = node.next.next
            node.next.next = tmp2
            node.next.next.next = tmp
            node = node.next.next
        
        return dummy.next

# @lc code=end

