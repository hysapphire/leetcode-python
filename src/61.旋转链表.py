#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        cnt = 1
        node = head
        while node.next:
            node = node.next
            cnt += 1
        node.next = head

        k = k % cnt

        node = head
        while cnt != k + 1:
            node = node.next
            cnt -= 1
        head = node.next
        node.next = None

        return head

# @lc code=end

