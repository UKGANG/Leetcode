'''
207 · Interval Sum II
https://www.lintcode.com/problem/207/
'''


class SegmentTreeNode:
    def __init__(self):
        self.left = None
        self.right = None

        self.left_node = None
        self.right_node = None

        self.val = None


class SegmentTree:
    def __init__(self, merge_func, arr):
        self.merge_func = merge_func
        self.root = self.build(0, len(arr) - 1, arr) if arr else None

    def build(self, l, r, arr):
        node = SegmentTreeNode()
        node.left, node.right = l, r
        if l == r:
            node.val = arr[l]
        else:
            m = l + ((r - l) >> 1)
            node.left_node = self.build(l, m, arr)
            node.right_node = self.build(m + 1, r, arr)
            node.val = self.merge_func(node.left_node.val, node.right_node.val)
        return node

    def _modify(self, idx, val, node):
        if not node.left <= idx <= node.right:
            return
        if node.left == node.right == idx:
            node.val = val
            return
        m = node.left + ((node.right - node.left) >> 1)
        if idx <= m:
            self._modify(idx, val, node.left_node)
        elif m + 1 <= idx:
            self._modify(idx, val, node.right_node)
        node.val = self.merge_func(node.left_node.val, node.right_node.val)

    def modify(self, idx, val):
        self._modify(idx, val, self.root)

    def _query(self, start, end, node):
        if start <= node.left <= node.right <= end:
            return node.val
        m = node.left + ((node.right - node.left) >> 1)
        if end <= m:
            return self._query(start, end, node.left_node)
        if m + 1 <= start:
            return self._query(start, end, node.right_node)
        return self.merge_func(
            self._query(start, end, node.left_node),
            self._query(start, end, node.right_node)
        )

    def query(self, start, end):
        return self._query(start, end, self.root)


class Solution:
    """
    @param: A: An integer array
    """

    def __init__(self, A):
        # do intialization if necessary
        self.segment_tree = SegmentTree(lambda a, b: a + b, A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """

    def query(self, start, end):
        # write your code here
        return self.segment_tree.query(start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """

    def modify(self, index, value):
        # write your code here
        self.segment_tree.modify(index, value)
