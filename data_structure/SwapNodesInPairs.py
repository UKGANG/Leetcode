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