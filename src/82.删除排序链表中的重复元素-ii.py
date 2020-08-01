#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("inf"))
        dummy.next = head
        node = head
        prev = dummy
        while node:
            val = node.val
            flag = False
            while node.next and node.next.val == val:
                flag = True
                node = node.next
            if flag:
                prev.next = node.next
            else:
                prev.next = node
                prev = node
            
            node = node.next
        
        return dummy.next

# @lc code=end

