#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue1 = deque()
        queue2 = deque()
        queue1.append(root)
        flag = True
        result = []
        while queue1:
            res = []
            while queue1:
                n = queue1.popleft()
                res.append(n.val)
                if n.left:
                    queue2.append(n.left)
                if n.right:
                    queue2.append(n.right)

            if not flag:
                res = res[::-1]
            result.append(res)
            queue1 = queue2
            queue2 = deque()
            flag = not flag

        return result

# @lc code=end

