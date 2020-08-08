#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.is_equal(p, q)

    def is_equal(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        
        return left.val == right.val and self.is_equal(left.left, right.left) and self.is_equal(left.right, right.right)
        
# @lc code=end

