#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.invert_tree(root)

    def invert_tree(self, root):
        if not root:
            return None
        
        t = root.left
        root.left = self.invert_tree(root.right)
        root.right = self.invert_tree(t)

        return root

    #     self.invert_tree(root)
    #     return root

    # def invert_tree(self, root):
    #     if not root:
    #         return
        
    #     t = root.left
    #     root.left = root.right
    #     root.right = t
    #     self.invert_tree(root.left)
    #     self.invert_tree(root.right)

# @lc code=end

