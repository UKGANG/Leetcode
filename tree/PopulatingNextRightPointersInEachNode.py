'''
116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            next_node = None
            for i in range(size):
                curr = curr_level.popleft()
                curr.next = next_node
                next_node = curr
                if curr.right:
                    curr_level.append(curr.right)
                if curr.left:
                    curr_level.append(curr.left)
        return root
