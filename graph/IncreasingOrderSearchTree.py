'''
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = [root]
        curr = root
        head = None
        while stack:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            curr = stack.pop()
            if not head:
                head = curr
                node = curr
            else:
                node.left = None
                node.right = curr
                node = curr

            if curr.right:
                stack.append(curr.right)
            curr = curr.right

        node.right = None
        node.left = None
        return head
