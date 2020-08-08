#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.is_balance(root) >= 0

    def is_balance(self, root):
        if not root:
            return 0
        
        left = self.is_balance(root.left)
        right = self.is_balance(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1


    #     flag, _ = self.is_balance(root)
    #     return flag

    # def is_balance(self, root):
    #     if not root:
    #         return True, 0
        
    #     left, left_height = self.is_balance(root.left)
    #     right, right_height = self.is_balance(root.right)

    #     return left and right and abs(left_height - right_height) <=1, max(left_height, right_height) + 1

# @lc code=end

