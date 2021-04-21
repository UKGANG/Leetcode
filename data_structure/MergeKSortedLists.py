'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
'''
import heapq
from typing import List

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [n for n in lists if n]
        priority_queue = []
        for idx, node in enumerate(lists):
            heapq.heappush(priority_queue, (node.val, idx))

        dummy = pointer = ListNode()
        while priority_queue:
            val, idx = heapq.heappop(priority_queue)
            pointer.next = lists[idx]
            if lists[idx].next:
                heapq.heappush(priority_queue, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next
            pointer = pointer.next
            pointer.next = None

        return dummy.next

    def mergeKLists_brute_force(self, lists: List[ListNode]) -> ListNode:
        lists = [n for n in lists if n]
        if not len(lists):
            return None
        result = []
        for node in lists:
            while node:
                result.append(node.val)
                node = node.next

        result.sort()

        result = [ListNode(val) for val in result]

        for i in range(len(result) - 1):
            result[i].next = result[i + 1]
        return result[0]

    def mergeKLists_slow(self, lists: List[ListNode]) -> ListNode:
        lists = [n for n in lists if n]
        if not len(lists):
            return None
        result = lists[0]
        for node in lists[1:]:
            result = self.mergeSort(result, node)
        return result

    def mergeSort(self, node_a: ListNode, node_b: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while node_a or node_b:
            if not node_a:
                curr.next = node_b
                node_b = None
            elif not node_b:
                curr.next = node_a
                node_a = None
            else:
                if node_a.val > node_b.val:
                    curr.next = node_b
                    node_b = node_b.next
                    curr.next.next = None

                    curr = curr.next
                else:
                    curr.next = node_a
                    node_a = node_a.next
                    curr.next.next = None

                    curr = curr.next
        return dummy.next

    def mergeKLists_deprecated(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        length = 0
        lists = [n for n in lists if n]
        while len(lists):
            # traverse list
            min_node = lists[0]
            min_idx = 0
            for idx, node in enumerate(lists):
                # pick the smallest node
                if node.val < min_node.val:
                    min_node = node
                    min_idx = idx
            lists[min_idx] = lists[min_idx].next
            if not lists[min_idx]:
                del lists[min_idx]
            length += 1
            self.insert_to_node(head, length, min_node)
            curr.next = min_node
            curr = curr.next
            min_node.next = None
        return head.next

    def insert_to_node(self, head: List[ListNode], length: int, node: ListNode) -> ListNode:
        if length == 1:
            head.next = node
            node.next = None
            return
        else:
            # Skip for dummy node
            head = head.next
        r = 0
        l = length
        while r < l:
            m = (r + l) >> 1
            m_node = self.get_nth_node(head, m)
            if m_node.val == node.val:
                node.next = m_node.next
                m_node.next = node.next
                return
            elif m_node.val < node.val:
                r = m + 1
            else:
                l = m
        m_node = self.get_nth_node(head, r)
        node.next = m_node.next
        m_node.next = node.next

    def get_nth_node(self, head: List[ListNode], n: int) -> ListNode:
        while n:
            if not head.next:
                return head
            head = head.next
            n -= 1
        return head


def build_nodes(node_list: List[List[int]]) -> ListNode:
    result = []
    for nodes in node_list:
        if len(nodes) == 0:
            continue
        elif len(nodes) == 1:
            result.append(ListNode(nodes[0]))
        else:
            nodes = list(reversed(nodes))
            prev = ListNode(nodes[0])
            for node in nodes[1:]:
                curr = ListNode(node)
                curr.next = prev
                prev = curr
            result.append(prev)

    return result


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


assert_value([1, 1, 2, 3, 4, 4, 5, 6], test_wrapper((Solution().mergeKLists)),
             lists=build_nodes([[1, 4, 5], [1, 3, 4], [2, 6]]))
assert_value([], test_wrapper((Solution().mergeKLists)), lists=build_nodes([]))
assert_value([], test_wrapper((Solution().mergeKLists)), lists=build_nodes([[]]))
assert_value([1, 1, 1, 2, 2, 2], test_wrapper((Solution().mergeKLists)), lists=build_nodes([[1, 2, 2], [1, 1, 2]]))
