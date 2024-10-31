'''
708. Insert into a Sorted Circular Linked List
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
'''
from typing import List

from test_tool import assert_value

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        prev, curr = head, head.next
        while prev.next != head:
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (prev.val <= insertVal or insertVal <= curr.val):
                break
            prev = prev.next
            curr = curr.next
        prev.next = new_node
        new_node.next = curr
        return head

    def _insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node_new = Node(insertVal)
        if not head:
            node_new.next = node_new
            return node_new

        if head == head.next:
            head.next = node_new
            node_new.next = head
            return head

        prev, curr = head, head.next

        while prev.next != head:
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val):
                break
            prev, curr = curr, curr.next

        node_new.next = curr
        prev.next = node_new

        return head


node1 = Node(3)
node2 = Node(3)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1

res = Solution().insert(node1, 0)
print(res)
