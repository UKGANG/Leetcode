'''
763. Partition Labels
https://leetcode.com/problems/partition-labels/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {}
        for idx, c in enumerate(s):
            cache[c] = idx
        l, r = 0, cache[s[0]]
        res = []
        for i in range(len(s)):
            r = max(r, cache[s[i]])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res

    def _partitionLabels(self, s: str) -> List[int]:
        cache = {}
        for idx, c in enumerate(s):
            cache[c] = cache.get(c, [idx, idx])
            cache[c][1] = idx
        intervals = sorted(cache.values())
        res = []
        l, r = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > r:
                res.append(r - l + 1)
                l, r = intervals[i]
            else:
                r = max(r, intervals[i][1])
            if r == len(s) - 1:
                res.append(r - l + 1)
                break
        return res
