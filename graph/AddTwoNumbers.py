"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = curr = ListNode()
        p1, p2 = l1, l2
        residual = 0

        while p1 or p2 or residual:
            curr.next = ListNode()
            curr = curr.next
            p1_val = 0 if not p1 else p1.val
            p2_val = 0 if not p2 else p2.val

            val = p1_val + p2_val + residual
            residual = 1 if val > 9 else 0
            val %= 10
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr.val = val

        return root.next
