#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

        # if m >= n:
        #     return head

        # dummy = ListNode(-1)
        # dummy.next = head
        # prev = dummy
        # node = head

        # i = 1
        # while node:
        #     if i == m:
        #         flag = node
        #         tmp = node.next
        #         node.next = None
        #         node = tmp
        #     elif m < i <= n:
        #         tmp = node.next
        #         node.next = prev.next
        #         prev.next = node
        #         node = tmp
        #     elif i == n + 1:
        #         flag.next = node
        #         node = node.next
        #     else:
        #         node = node.next
        #         prev = prev.next
        #     i += 1

        # return dummy.next

# @lc code=end

