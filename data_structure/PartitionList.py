'''
86. Partition List
https://leetcode.com/problems/partition-list/
'''
from typing import List

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_dummy = ListNode()
        large_dummy = ListNode()

        small_cursor = small_dummy
        large_cursor = large_dummy

        while head:
            if head.val < x:
                small_cursor.next = head
                small_cursor = small_cursor.next
            else:
                large_cursor.next = head
                large_cursor = large_cursor.next
            head = head.next

        small_cursor.next = large_dummy.next

        large_cursor.next = None

        return small_dummy.next


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


assert_value([1, 2, 2, 4, 3, 5], test_wrapper(Solution().partition), head=build_nodes([1, 4, 3, 2, 5, 2]), x=3)
assert_value([1, 2], test_wrapper(Solution().partition), head=build_nodes([2, 1]), x=2)
