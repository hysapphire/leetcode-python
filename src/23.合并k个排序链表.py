#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while True:
            all_none = True
            min_idx = 10000
            min_value = 10000
            for idx, list_ in enumerate(lists):
                if list_ is not None:
                    if list_.val < min_value:
                        min_value = list_.val
                        min_idx = idx
                    all_none = False
            
            if all_none:
                return dummy.next
            
            head.next = lists[min_idx]
            head = head.next
            lists[min_idx] = lists[min_idx].next

# @lc code=end

