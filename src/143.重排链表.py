#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        second = self.reverse(second)
          
        node = head
        while node and second:
            tmp1 = node.next
            node.next = second
            tmp2 = second.next
            second.next = tmp1
            node = tmp1
            second = tmp2
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return new_head
        

# @lc code=end

