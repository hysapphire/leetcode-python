#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 1
        self.func(root)
        return self.max - 1

    def func(self, root):
        if not root:
            return 0
        
        left = self.func(root.left)
        right = self.func(root.right)
        self.max = max(self.max, left + right + 1)
        return max(left, right) + 1

# @lc code=end

