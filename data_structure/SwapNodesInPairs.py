'''
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        node_prev = dummy_head
        node_curr = head
        while node_curr and node_curr.next:
            node_1 = node_curr
            node_2 = node_1.next if node_1 else None
            node_next = node_2.next if node_2 else None

            node_prev.next = node_2
            node_1.next = node_next
            if node_2:
                node_2.next = node_1

            node_curr = node_next
            node_prev = node_1

        return dummy_head.next

    def _swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        head = dummy
        while head and head.next and head.next.next:
            node1, node2 = head.next, head.next.next
            node1.next, node2.next = node2.next, node1

            head.next = node2
            head = node1

        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

res = Solution().swapPairs(node1)
res
