'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
'''
from typing import List
from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        stack = []
        while head:
            stack.append(head)
            head = head.next

        head = stack.pop()
        curr = head
        while len(stack):
            curr.next = stack.pop()
            curr = curr.next

        curr.next = None
        return head


def build_nodes(nodes: List[int]) -> ListNode:
    if len(nodes) == 0:
        return []
    if len(nodes) == 1:
        return ListNode(nodes[0])
    return ListNode(nodes[0], build_nodes(nodes[1:]))


def to_array(node: ListNode):
    nodes = []
    while node:
        nodes.append(node.val)
        node = node.next
    return nodes


def test_wrapper(func):
    def func_wrapper(**kwargs):
        res = func(**kwargs)
        return to_array(res)

    return func_wrapper


assert_value([5, 4, 3, 2, 1], test_wrapper(Solution().reverseList), head=build_nodes([1, 2, 3, 4, 5]))
