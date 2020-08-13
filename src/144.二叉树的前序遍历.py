#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        
        return result

    #     result = []
    #     self.preorder_traversal(root, result)
    #     return result

    # def preorder_traversal(self, root, result):
    #     if not root:
    #         return
        
    #     result.append(root.val)
    #     self.preorder_traversal(root.left, result)
    #     self.preorder_traversal(root.right, result)

# @lc code=end

