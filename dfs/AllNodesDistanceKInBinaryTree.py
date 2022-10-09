'''
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if not node:
                return -1
            if node.val == target.val:
                self._traverse_subtree(node, k, res)
                return 0

            dist_left = dfs(node.left)
            dist_right = dfs(node.right)

            dist = -1
            if dist_left > -1:
                dist = dist_left + 1
                if dist == k:
                    res.append(node.val)
                elif dist < k:
                    # Search right
                    self._traverse_subtree(node.right, k - dist - 1, res)

            if dist_right > -1:
                dist = dist_right + 1
                if dist == k:
                    res.append(node.val)
                elif dist < k:
                    # Search left
                    self._traverse_subtree(node.left, k - dist - 1, res)
            return dist

        res = []
        dfs(root)

        return res

    def _traverse_subtree(self, node, k, res):
        curr_level = collections.deque([node])
        while curr_level:
            size = len(curr_level)
            for _ in range(size):
                curr = curr_level.popleft()
                if not curr:
                    continue
                if not k:
                    res.append(curr.val)
                else:
                    curr_level.append(curr.left)
                    curr_level.append(curr.right)
            k -= 1
