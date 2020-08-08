#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []
        
        d = {}

        def generate(start, end):
            if start > end:
                return [None]
            
            if (start, end) in d:
                return d[(start, end)]
            
            result = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            
            d[(start, end)] = result
            return result
        
        return generate(1, n)

# @lc code=end

