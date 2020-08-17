#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = ""
        result = []
        self.dfs(root, path, result)
        return result

    def dfs(self, root, path, result):
        if not root:
            return
        if not root.left and not root.right:
            t = path + "->" + str(root.val)
            result.append(t[2:])
            return

        if root.left:
            self.dfs(root.left, path + "->" + str(root.val), result)
        if root.right:
            self.dfs(root.right, path + "->" + str(root.val), result)

# @lc code=end

