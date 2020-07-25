#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        # dummy_odd = ListNode(-1)
        # dummy_even = ListNode(-1)

        # odd = head
        # even = head.next
        # dummy_odd.next = odd
        # dummy_even.next = even

        # head = head.next.next
        # while head and head.next:
        #     odd.next = head
        #     odd = odd.next
        #     head = head.next
        #     even.next = head
        #     even = even.next
        #     head = head.next
        # if head:
        #     odd.next = head
        #     odd = odd.next
        # even.next = None

        # odd.next = dummy_even.next

        # return dummy_odd.next

        odd = head
        even = head.next
        odd_head = odd
        even_head = even

        head = head.next.next
        while head and head.next:
            odd.next = head
            odd = odd.next
            head = head.next
            even.next = head
            even = even.next
            head = head.next
        if head:
            odd.next = head
            odd = odd.next
        even.next = None

        odd.next = even_head

        return odd_head


# @lc code=end

