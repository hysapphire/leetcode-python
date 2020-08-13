#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]
        last = None
        left = True
        while stack:
            while stack[-1].left and left:
                stack.append(stack[-1].left)
            if stack[-1].right and stack[-1].right != last:
                stack.append(stack[-1].right)
                left = True
                continue
            node = stack.pop()
            last = node
            left = False
            result.append(node.val)
        
        return result



        # result = []
        # stack = []
        # last = None
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack[-1]
        #     if curr.right and curr.right != last:
        #         curr = curr.right
        #         continue
            
        #     result.append(curr.val)
        #     stack.pop()
        #     last = curr
        #     curr = None
        
        # return result


        # if not root:
        #     return []

        # result = []
        # stack = [root]
        # visited = set()
        # while stack:
        #     while stack[-1].left:
        #         if stack[-1].left in visited:
        #             break
        #         stack.append(stack[-1].left)
        #     if stack[-1].right and stack[-1].right not in visited:
        #         stack.append(stack[-1].right)
        #         continue
        #     node = stack.pop()
        #     visited.add(node)
        #     result.append(node.val)
        
        # return result


    #     result = []
    #     self.postorder_traversal(root, result)
    #     return result

    # def postorder_traversal(self, root, result):
    #     if not root:
    #         return
        
    #     self.postorder_traversal(root.left, result)
    #     self.postorder_traversal(root.right, result)
    #     result.append(root.val)

# @lc code=end

