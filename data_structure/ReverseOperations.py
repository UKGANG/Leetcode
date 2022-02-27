'''
Reverse Operations
https://leetcode.com/discuss/interview-question/688086/fb-online-practice-question
'''
from test_tool import assert_value


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Add any helper functions you may need here


def reverse(head):
    # Write your code here
    stack = []
    root = Node(None)
    root.next = head

    curr, prev = head, root
    while curr:
        if curr.data & 1:
            while stack:
                prev.next = stack.pop()
                prev = prev.next
            prev.next = curr
            prev = curr
        else:
            stack.append(curr)
        curr = curr.next

    while stack:
        prev.next = stack.pop()
        prev = prev.next
    prev.next = curr

    return root.next


def conver_result(root):
    res = []
    while root:
        res.append(root.data)
        root = root.next
    return res


# TC1
root = Node(None)
curr = root
for n in [1, 2, 8, 9, 12, 16]:
    curr.next = Node(n)
    curr = curr.next

root = reverse(root.next)
assert_value([1, 8, 2, 9, 16, 12], conver_result, root=root)

# TC2
root = Node(None)
curr = root
for n in [2, 18, 24, 3, 5, 7, 9, 6, 12]:
    curr.next = Node(n)
    curr = curr.next

root = reverse(root.next)
assert_value([24, 18, 2, 3, 5, 7, 9, 12, 6], conver_result, root=root)
