#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.dfs(root, sum, [])
    
    def dfs(self, root, sum, sum_list):
        if not root:
            return 0

        sum_list = [root.val + num for num in sum_list] + [root.val]

        return sum_list.count(sum) + self.dfs(root.left, sum, sum_list) + \
            self.dfs(root.right, sum, sum_list)        

# @lc code=end

