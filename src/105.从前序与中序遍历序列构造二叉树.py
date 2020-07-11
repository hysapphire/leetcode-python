#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build_tree(preorder, inorder)

    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root_idx = inorder.index(root_val)

        left_num = root_idx

        node = TreeNode(root_val)
        node.left = self.build_tree(preorder[1:left_num+1], inorder[:left_num])
        node.right = self.build_tree(preorder[left_num+1:], inorder[left_num+1:])

        return node

# @lc code=end

