#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        fast_pointer = head
        slow_pointer = head

        for _ in range(n):
            fast_pointer = fast_pointer.next
        
        # if fast_pointer is None:
        #     return head.next

        # while fast_pointer.next is not None:
        #     fast_pointer = fast_pointer.next
        #     slow_pointer = slow_pointer.next
        
        # slow_pointer.next = slow_pointer.next.next

        while fast_pointer is not None:
            fast_pointer = fast_pointer.next
            prev = slow_pointer
            slow_pointer = slow_pointer.next
        
        prev.next = slow_pointer.next
        
        return dummy.next

# @lc code=end

