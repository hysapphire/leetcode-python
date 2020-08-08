#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return self.dfs(nums)

    def dfs(self, nums):
        if not nums:
            return None

        idx = len(nums) // 2
        node = TreeNode(nums[idx])
        node.left = self.dfs(nums[:idx])
        node.right = self.dfs(nums[idx+1:])
        return node

# @lc code=end

