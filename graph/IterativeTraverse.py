'''
Iterative Traverse
'''


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_traverse(root: Node):
    stack = [root]
    while stack:
        node = stack.pop()
        visit_node(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def in_order_traverse(root: Node):
    stack = [root]
    curr = root
    while stack:
        while curr:
            curr = curr.left
            if curr:
                stack.append(curr)
        curr = stack.pop()
        visit_node(curr)
        curr = curr.right
        if curr:
            stack.append(curr)


def post_order_traverse(root: Node):
    stack = []
    curr = root
    while True:
        while curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        if curr.right and stack and curr.right == stack[-1]:
            stack.pop()
            stack.append(curr)
            curr = curr.right
        else:
            visit_node(curr)
            curr = None

        if not stack:
            break


def visit_node(node: Node):
    print(node.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# 4 5 2 6 7 3 1
post_order_traverse(root)


# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(5)
# root.right.left = Node(2)
# # 10 8 3 5 2 2
# pre_order_traverse(root)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# # 4 2 5 1 3
# in_order_traverse(root)