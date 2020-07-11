#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float("inf")
        self.max_path_sum(root)
        return self.max_sum

    def max_path_sum(self, root):
        if not root:
            return 0

        left_max_sum = max(self.max_path_sum(root.left), 0)
        right_max_sum = max(self.max_path_sum(root.right), 0)

        self.max_sum = max(self.max_sum, left_max_sum + right_max_sum + root.val)

        return max(left_max_sum, right_max_sum) + root.val

# @lc code=end

