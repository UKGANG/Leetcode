'''
Nodes in a Subtree
https://leetcode.com/discuss/interview-question/756125/facebook-recruiting-portal-nodes-in-a-subtree
'''
import collections
from test_tool import assert_value


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []
        self.cache = collections.defaultdict(lambda: 0)


# Add any helper functions you may need here
def dfs(node, c, s):
    if not node:
        return

    # prepare for cache
    if c not in node.cache:
        for child in node.children:
            dfs(child, c, s)
            node.cache[c] += child.cache[c] if child else 0
        if c == s[node.val - 1]:
            node.cache[c] += 1


def count_of_nodes(root, queries, s):
    # Write your code here
    # prepare for cache
    for u, c in queries:
        dfs(root, c, s)
    res = []
    for u, c in queries:
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == u:
                res.append(curr.cache[c])
                break
            [stack.append(child) for child in curr.children]

    return res


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.children = [node2, node3]

assert_value([2], count_of_nodes, root=root, queries=[[1, 'a']], s='aba')

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node2.children = [node4, node5]
node3.children = [node6]
root.children = [node2, node3, node7]

assert_value([4, 1, 2], count_of_nodes, root=root, queries=[[1, 'a'], [2, 'b'], [3, 'a']], s='abaacab')
