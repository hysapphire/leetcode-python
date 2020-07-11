#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_symmetric(root, root)

    def is_symmetric(self, left, right):
        queue = []
        queue.append(left)
        queue.append(right)

        while queue:
            left = queue[0]
            right = queue[1]
            queue = queue[2:]
            if not left and not right:
                continue
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True

    #     if not root:
    #         return True

    #     return self.is_symmetric(root.left, root.right)

    # def is_symmetric(self, left, right):
    #     if not left and not right:
    #         return True
        
    #     if not left or not right:
    #         return False
        
    #     if left.val == right.val:
    #         return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)
    #     else:
    #         return False
        
# @lc code=end

