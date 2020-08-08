#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.dfs(root, nodes)
        tmp = []
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i+1].val:
                tmp.append(nodes[i])
                tmp.append(nodes[i+1])

        if len(tmp) == 2:
            tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val
        elif len(tmp) == 4:
            tmp[0].val, tmp[3].val = tmp[3].val, tmp[0].val
    
    def dfs(self, root, nodes):
        if not root:
            return
        self.dfs(root.left, nodes)
        nodes.append(root)
        self.dfs(root.right, nodes)
        
# @lc code=end

