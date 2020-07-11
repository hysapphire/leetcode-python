#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head.next
        fast = head.next.next

        cnt = 1
        while slow != fast:
            if not fast or not fast.next:
                return None
            
            slow = slow.next
            fast = fast.next.next
            cnt += 1

        fast = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

        
# @lc code=end

