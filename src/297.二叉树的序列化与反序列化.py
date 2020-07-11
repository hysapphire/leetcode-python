#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return str([])

        queue = deque()
        result = []
        queue.append(root)
        while queue:
            r = queue.popleft()
            if not r:
                result.append(None)
                continue
            result.append(r.val)
            queue.append(r.left)
            queue.append(r.right)

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(eval(data))
        if not data:
            return None
        node = TreeNode(data[0])
        data.popleft()
        head = node
        de_data = deque([node])

        while data and de_data:
            node = de_data.popleft()

            r = data.popleft()
            if r is not None:
                left = TreeNode(r)
                node.left = left
                de_data.append(left)
            
            r = data.popleft()
            if r is not None:
                right = TreeNode(r)
                node.right = right
                de_data.append(right)

        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

