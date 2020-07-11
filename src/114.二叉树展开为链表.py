#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_list(root)

    def flatten_list(self, root):
        if not root:
            return None
        
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            prev = root.left
            while prev.right:
                prev = prev.right
            prev.right = root.right
            root.right = root.left
            root.left = None

    #     self.prev = None
    #     self.flatten_list(root)

    # def flatten_list(self, root):
    #     if not root:
    #         return None
        
    #     self.flatten_list(root.right)
    #     self.flatten_list(root.left)
    #     root.right = self.prev
    #     root.left = None
    #     self.prev = root
        
# @lc code=end

