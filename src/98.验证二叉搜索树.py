#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:    
        return self.check_valid(root, -float("inf"), float("inf"))

    def check_valid(self, root, lower, upper):
        if not root:
            return True
        
        if lower < root.val < upper:
            return self.check_valid(root.left, lower, root.val) and self.check_valid(root.right, root.val, upper)
        
        return False

# @lc code=end

