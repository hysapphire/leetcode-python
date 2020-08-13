#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        next_ = head
        last = head
        while next_:
            if next_.val < last.val:
                node = dummy.next
                prev = dummy
                while node.val < next_.val:
                    prev = node
                    node = node.next
                
                tmp = next_.next
                prev.next = next_
                next_.next = node
                last.next = tmp
                next_ = tmp
            else:
                last = next_
                next_ = next_.next
        
        return dummy.next
                
# @lc code=end

