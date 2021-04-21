'''
148. Sort List
https://leetcode.com/problems/sort-list/
'''
from typing import List

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                prev = head
                curr = head.next
                curr.next = prev
                prev.next = None
                return curr
            else:
                return head

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        left = head
        right = slow.next
        slow.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        res_head = ListNode()
        res = res_head
        while left or right:
            if not left:
                res.next = right
                right = right.next
            elif not right:
                res.next = left
                left = left.next
            else:
                if right.val > left.val:
                    res.next = left
                    left = left.next
                else:
                    res.next = right
                    right = right.next

            res = res.next
        return res_head.next


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


assert_value([1, 2, 3, 4], test_wrapper(Solution().sortList), head=build_nodes([4, 2, 1, 3]))
assert_value([-1, 0, 3, 4, 5], test_wrapper(Solution().sortList), head=build_nodes([-1, 5, 3, 4, 0]))
assert_value([], test_wrapper(Solution().sortList), head=build_nodes([]))
assert_value([0, 1, 1, 2, 2, 3, 4], test_wrapper(Solution().sortList), head=build_nodes([4, 2, 1, 3, 2, 1, 0]))
