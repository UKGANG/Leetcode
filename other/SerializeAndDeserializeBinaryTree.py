'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''
from typing import List

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            val = str(node.val) if node else 'null'
            res.append(val)
            if node:
                q.append(node.left)
                q.append(node.right)

        idx = len(res) - 1
        while 'null' == res[idx]:
            idx -= 1
        res = res[:idx + 1]
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(' ')
        nodes = [TreeNode(int(val)) if 'null' != val else None for val in nodes]

        idx_root = 0

        for idx_leaf in range(1, len(nodes), 2):
            left = idx_leaf
            right = idx_leaf + 1
            nodes[idx_root].left = nodes[left]
            if right >= len(nodes):
                break
            nodes[idx_root].right = nodes[right]
            idx_root += 1
            while not nodes[idx_root]:
                idx_root += 1

        return nodes[0]


# Your Codec object will be instantiated and called as such:

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
root.left = node2
root.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
