#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(-1)
        big = ListNode(-1)
        small_head = small
        big_head = big
        node = head

        while node:
            if node.val < x:
                small.next = node
                tmp = node.next
                node.next = None
                node = tmp
                small = small.next
            else:
                big.next = node
                tmp = node.next
                node.next = None
                node = tmp
                big = big.next

        small.next = big_head.next

        return small_head.next

        # dummy = ListNode(-1)
        # dummy.next = head
        # prev = dummy
        # node = head
        # pos = dummy

        # while node:
        #     if node.val < x:
        #         if pos == prev:
        #             prev = node
        #             node = node.next
        #             pos = pos.next
        #             continue
        #         tmp1 = pos.next
        #         pos.next = node
        #         prev.next = node.next
        #         node.next = tmp1
        #         node = prev.next
        #         pos = pos.next
        #     else:
        #         prev = node
        #         node = node.next
        
        # return dummy.next

# @lc code=end

