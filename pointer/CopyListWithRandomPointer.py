'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
'''
from typing import List

from test_tool import assert_value

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache_old = {}
        dummy_old = Node(-1, head)
        curr_old = dummy_old
        cnt = 0
        while curr_old:
            cache_old[curr_old] = cnt
            curr_old = curr_old.next
            cnt += 1

        curr_old = dummy_old.next
        dummy_new = Node(-1, None)
        prev_new = dummy_new

        cache_new = [dummy_new]
        while curr_old:
            curr_new = Node(curr_old.val, None)
            prev_new.next = curr_new

            cache_new.append(curr_new)

            curr_old = curr_old.next
            prev_new = curr_new

        curr_old = dummy_old
        curr_new = dummy_new
        while curr_old:
            if curr_old.random:
                idx = cache_old[curr_old.random]
                curr_new.random = cache_new[idx]
            curr_old = curr_old.next
            curr_new = curr_new.next

        return dummy_new.next

    def _copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. Calculate sequences
        dummy_orig = Node(-1, head)
        nodes_orig = {}
        idx = 0
        curr_orig = dummy_orig
        while True:
            curr_orig = curr_orig.next
            if not curr_orig:
                break
            nodes_orig[curr_orig] = idx
            idx += 1

        # 2. Calculate sequences index
        random_index_orig = []
        curr_orig = dummy_orig
        while True:
            curr_orig = curr_orig.next
            if not curr_orig:
                break
            if curr_orig.random:
                random_index_orig.append(nodes_orig[curr_orig.random])
            random_index_orig.append(None)

        # 3. Create new nodes
        dummy_new = Node(-1)
        nodes_new = []
        curr_orig = dummy_orig
        curr_new = dummy_new
        while True:
            curr_orig = curr_orig.next
            if not curr_orig:
                break
            curr_new.next = Node(curr_orig.val)
            curr_new = curr_new.next
            nodes_new.append(curr_new)

        curr_orig = dummy_orig
        curr_new = dummy_new
        idx = 0
        while curr_orig:
            if curr_orig.random:
                curr_new.random = nodes_new[nodes_orig[curr_orig.random]]
            curr_orig = curr_orig.next
            curr_new = curr_new.next
            idx += 1

        return dummy_new.next
