#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1

        # cnt1 = 0
        # l1 = headA
        # while l1:
        #     l1 = l1.next
        #     cnt1 += 1
        
        # cnt2 = 0
        # l2 = headB
        # while l2:
        #     l2 = l2.next
        #     cnt2 += 1
        
        # l1 = headA
        # l2 = headB
        # for _ in range(cnt1 - cnt2):
        #     l1 = l1.next
        # for _ in range(cnt2 - cnt1):
        #     l2 = l2.next
        
        # while l1 != l2:
        #     l1 = l1.next
        #     l2 = l2.next
        
        # return l1
        
# @lc code=end

