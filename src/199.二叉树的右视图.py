#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        q = [root]

        while q:
            result.append(q[-1].val)
            p = []
            for qq in q:
                if qq.left:
                    p.append(qq.left)
                if qq.right:
                    p.append(qq.right)
            q = p

        return result

# @lc code=end

