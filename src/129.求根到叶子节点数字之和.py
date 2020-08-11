#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, s):
        if not root:
            return 0
        
        tmp = s * 10 + root.val
        if not root.left and not root.right:
            return tmp

        return self.dfs(root.left, tmp) + self.dfs(root.right, tmp)


    #     path = 0
    #     result = []
    #     self.dfs(root, path, result)
    #     return sum(result)

    # def dfs(self, root, path, result):
    #     if not root:
    #         return
    #     if not root.left and not root.right:
    #         result.append(path * 10 + root.val)
    #         return
        
    #     self.dfs(root.left, path * 10 + root.val, result)
    #     self.dfs(root.right, path * 10 + root.val, result)

# @lc code=end

