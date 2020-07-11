#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convert_BST(root, 0)
        return root

    def convert_BST(self, root, last):
        if not root:
            return 0 + last
        right = self.convert_BST(root.right, last)
        root.val = root.val + right
        return self.convert_BST(root.left, root.val)

# @lc code=end

