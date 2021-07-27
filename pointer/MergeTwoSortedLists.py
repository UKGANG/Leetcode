'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
'''
from typing import List

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(-1)

        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummy.next
