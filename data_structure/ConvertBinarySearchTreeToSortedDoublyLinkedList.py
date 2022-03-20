'''
1534 · Convert Binary Search Tree to Sorted Doubly Linked List
https://www.lintcode.com/problem/1534/
'''


"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        curr = root
        dummy = TreeNode(None)
        head = dummy
        stack = [root]
        while True:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            curr = stack.pop()
            head.right = curr
            curr.left = head
            head = curr
            if curr.right:
                stack.append(curr.right)
            if not stack:
                curr.right = dummy.right
                dummy.right.left = curr
                break
            curr = curr.right
        return dummy.right


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node4.left = node2
node4.right = node5
node2.left = node1
node2.right = node3

res = Solution().treeToDoublyList(node4)
print(res)