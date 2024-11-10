"""
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary
"""
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nodes = set(''.join(words))
        graph = collections.defaultdict(list)
        indegree = collections.Counter()

        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                graph[c1].append(c2)
                indegree[c2] += 1
                break
            else:
                if len(word1) > len(word2):
                    return ''

        queue = collections.deque([node for node in nodes if indegree[node] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for c in graph[c]:
                indegree[c] -= 1
                if not indegree[c]:
                    queue.append(c)

        return ''.join(res) if len(res) == len(nodes) else ''
