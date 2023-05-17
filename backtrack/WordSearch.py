"""
79. Word Search
https://leetcode.com/problems/word-search
"""
import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, node):
            nonlocal m, n
            c = board[x][y]
            if c not in node.child:
                return False
            if not node.child[c].child:
                return True
            board[x][y] = None

            for dx, dy in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]:
                if not 0 <= x + dx < m or not 0 <= y + dy < n:
                    continue
                if dfs(x + dx, y + dy, node.child[c]):
                    return True
            else:
                board[x][y] = c
                return False

        root = TrieNode()
        curr = root
        for c in word:
            curr = curr.child[c]
        m, n = len(board), len(board[0])
        for x, y in itertools.product(range(m), range(n)):
            if dfs(x, y, root):
                return True
        else:
            return False
