#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


    #     return self.dfs(root)[k-1]

    # def dfs(self, root):
    #     return self.dfs(root.left) + [root.val] + self.dfs(root.right) if root else []

    #     result = []
    #     self.dfs(root, result)
    #     return result[k-1]

    # def dfs(self, root, result):
    #     if not root:
    #         return
    #     self.dfs(root.left, result)
    #     result.append(root.val)
    #     self.dfs(root.right, result)
        
# @lc code=end