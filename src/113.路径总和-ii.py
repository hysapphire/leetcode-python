#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path = []
        result = []
        self.dfs(root, sum, path, result)
        return result

    def dfs(self, root, gap, path, result):
        if not root:
            return
        
        path.append(root.val)
        if not root.left and not root.right:
            if gap == root.val:
                result.append(path[:])
        else:
            self.dfs(root.left, gap - root.val, path, result)
            self.dfs(root.right, gap - root.val, path, result)
        path.pop()

# @lc code=end

