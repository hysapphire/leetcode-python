#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        cur = [root]
        nex = []
        while True:
            if not cur:
                break
            res = []
            for c in cur:
                res.append(c.val)
                if c.left:
                    nex.append(c.left)
                if c.right:
                    nex.append(c.right)

            result.append(res)
            cur = nex
            nex = []
        
        return result[::-1]

# @lc code=end

