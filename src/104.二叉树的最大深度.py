#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.max_depth(root)

    def max_depth(self, root):
        if not root:
            return 0
        
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

# @lc code=end

