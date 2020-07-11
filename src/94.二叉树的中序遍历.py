#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        result = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)

            cur = cur.right
        
        return result

        
    #     if root is None:
    #         return []

    #     result = []
    #     self.inorder(root, result)
    #     return result
    
    # def inorder(self, head, result):
    #     if head.left is not None:
    #         self.inorder(head.left, result)
    #     result.append(head.val)
    #     if head.right is not None:
    #         self.inorder(head.right, result)

# @lc code=end

