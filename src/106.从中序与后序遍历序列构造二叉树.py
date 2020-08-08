#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.dfs(inorder, postorder)

    def dfs(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        node = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        node.left = self.dfs(inorder[:idx], postorder[:idx])
        node.right = self.dfs(inorder[idx+1:], postorder[idx:-1])
        
        return node

# @lc code=end

