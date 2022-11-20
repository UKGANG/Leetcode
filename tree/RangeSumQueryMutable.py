'''
307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/
'''
from typing import List, NoReturn


class SegmentTreeNode:
    def __init__(self):
        self.left_val = None
        self.right_val = None

        self.left_node = None
        self.right_node = None

        self.val = None


class NumArray:
    def __init__(self, nums: List[int]):
        self.merge_func = lambda a, b: a + b
        self.root = self.build(0, len(nums) - 1, nums)

    def build(self, left, right, nums) -> SegmentTreeNode:
        node = SegmentTreeNode()
        node.left_val = left
        node.right_val = right

        if left == right:
            node.val = nums[right]
        else:
            m = left + ((right - left) >> 1)
            left_node = self.build(left, m, nums)
            right_node = self.build(m + 1, right, nums)
            node.left_node = left_node
            node.right_node = right_node
            node.val = self.merge_func(left_node.val, right_node.val)
        return node

    def _update(self, index: int, val: int, node) -> NoReturn:
        if not node.left_val <= index <= node.right_val:
            return
        if node.left_val == node.right_val == index:
            node.val = val
            return

        m = node.left_val + ((node.right_val - node.left_val) >> 1)
        if index <= m:
            self._update(index, val, node.left_node)
        elif m + 1 <= index:
            self._update(index, val, node.right_node)
        node.val = self.merge_func(node.left_node.val, node.right_node.val)

    def update(self, index: int, val: int) -> None:
        self._update(index, val, self.root)

    def _query(self, left: int, right: int, node) -> int:
        if node.right_val < left or node.left_val > right:
            return 0
        if left <= node.left_val <= node.right_val <= right:
            return node.val
        m = node.left_val + ((node.right_val - node.left_val) >> 1)
        if right <= m:
            return self._query(left, right, node.left_node)
        elif m + 1 <= left:
            return self._query(left, right, node.right_node)
        left_val = self._query(left, right, node.left_node)
        right_val = self._query(left, right, node.right_node)
        return self.merge_func(left_val, right_val)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(left, right, self.root)
