'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
'''
from typing import List

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
