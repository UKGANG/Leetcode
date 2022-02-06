'''
19. Remove Nth Node From End of List
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=827844&ctid=232494
'''
from typing import List, Optional

from test_tool import assert_value


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        if n == len(stack):
            return head.next
        prev = stack[-(n + 1)]
        curr = None
        if n > 1:
            curr = stack[-(n - 1)]
        prev.next = curr
        return head


fifth = ListNode(5, None)
fourth = ListNode(4, fifth)
third = ListNode(3, fourth)
second = ListNode(2, third)
first = ListNode(1, second)

res = Solution().removeNthFromEnd(first, 2)
print(res)
