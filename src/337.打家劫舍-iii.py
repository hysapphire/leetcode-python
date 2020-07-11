#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        result = [0, 0]
        result[0] = max(left) + max(right)
        result[1] = left[0] + right[0] + root.val

        return result


    #     d = {}
    #     return self.dfs(root, 0, False, d)

    # def dfs(self, root, total, is_used, d):
    #     if not root:
    #         return 0

    #     if root in d:
    #         if is_used in d[root]:
    #             return d[root][is_used]
            
    #     max_profit = 0
    #     max_profit = max(max_profit, self.dfs(root.left, total, False, d) + self.dfs(root.right, total, False, d))
    #     if not is_used:
    #         max_profit = max(max_profit, self.dfs(root.left, total + root.val, True, d) + self.dfs(root.right, total + root.val, True, d) + root.val)
        
    #     d[root] = {}
    #     d[root][is_used] = max_profit
    #     return max_profit

# @lc code=end

