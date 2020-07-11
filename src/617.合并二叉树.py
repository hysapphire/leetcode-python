#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.merge_tree(t1, t2)

    def merge_tree(self, t1, t2):
        if not t1 and not t2:
            return None
        
        root = TreeNode(0)
        root.val = (t1.val if t1 else 0) + (t2.val if t2 else 0)

        if t1 and t2:
            root.left = self.merge_tree(t1.left, t2.left)
            root.right = self.merge_tree(t1.right, t2.right)
        elif t1:
            root.left = self.merge_tree(t1.left, None)
            root.right = self.merge_tree(t1.right, None)
        else:
            root.left = self.merge_tree(None, t2.left)
            root.right = self.merge_tree(None, t2.right)
        
        return root



    #     if not t1 and not t2:
    #         return None
    #     root = TreeNode(0)
    #     self.merge_tree(t1, t2, root)
    #     return root

    # def merge_tree(self, t1, t2, root):
    #     if not t1 and not t2:
    #         return
    #     root.val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
        
        
    #     if t1 and t2:
    #         if t1.left or t2.left:
    #             root.left = TreeNode(0)
    #             self.merge_tree(t1.left, t2.left, root.left)
    #         if t1.right or t2.right:
    #             root.right = TreeNode(0)
    #             self.merge_tree(t1.right, t2.right, root.right)
    #         return

    #     if t1:
    #         if t1.left:
    #             root.left = TreeNode(0)
    #             self.merge_tree(t1.left, None, root.left)
    #         if t1.right:
    #             root.right = TreeNode(0)
    #             self.merge_tree(t1.right, None, root.right)     
    #         return
        
    #     if t2:
    #         if t2.left:
    #             root.left = TreeNode(0)
    #             self.merge_tree(None, t2.left, root.left)
    #         if t2.right:
    #             root.right = TreeNode(0)
    #             self.merge_tree(None, t2.right, root.right)
    #     return
# @lc code=end

