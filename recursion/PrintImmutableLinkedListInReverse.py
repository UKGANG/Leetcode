"""
1265. Print Immutable Linked List in Reverse
https://leetcode.com/problems/print-immutable-linked-list-in-reverse/description/
"""


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head.getNext():
            self.printLinkedListInReverse(head.getNext())
        head.printValue()
