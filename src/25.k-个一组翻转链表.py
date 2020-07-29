#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            tmp = tail.next
            head, tail = self.reverse_list(head, tail)

            pre.next = head
            tail.next = tmp
            pre = tail
            head = tail.next
        
        return dummy.next
        

    def reverse_list(self, head, tail):
        prev = tail.next
        node = head
        while prev != tail:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return tail, head


# @lc code=end

