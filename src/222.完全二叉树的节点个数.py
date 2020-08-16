#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        d = 0
        node = root
        while node.left:
            d += 1
            node = node.left
        
        if d == 0:
            return 1
        
        left, right = 1, 2 ** d - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exists(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2 ** d - 1 + left

    def exists(self, idx, d, node):
        left, right = 0, 2**d - 1
        for _ in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None



        # return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0



        # if not root:
        #     return 0

        # q = deque([root])
        # cnt = 0
        # while q:
        #     n = q.popleft()
        #     cnt += 1
        #     if n.left:
        #         q.append(n.left)
        #     if n.right:
        #         q.append(n.right)
        
        # return cnt

# @lc code=end

