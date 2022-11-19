'''
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            # 1. Record nodes to swap
            window = []
            for _ in range(k):
                if not curr:
                    break
                window.append(curr)
                curr = curr.next
            if k > len(window):
                break

            # 2. Swap nodes
            while window:
                prev.next = window[-1]
                prev = window.pop()
            prev.next = curr

            # 3. Move the pointer to the next place

        return dummy.next
