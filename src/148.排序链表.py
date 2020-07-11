#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.sort_list(head)

    def sort_list(self, head):
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        l1 = self.sort_list(head)
        l2 = self.sort_list(mid)

        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:    
        dummy = ListNode(-1)
        head = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        head.next = l1 if l1 else l2

        return dummy.next
# @lc code=end

