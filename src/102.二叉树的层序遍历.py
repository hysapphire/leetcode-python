#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            r = []
            next_queue = []
            for q in queue:
                r.append(q.val)
                if q.left:
                    next_queue.append(q.left)
                if q.right:
                    next_queue.append(q.right)
            result.append(r)
            queue = next_queue
        
        return result   

# @lc code=end

