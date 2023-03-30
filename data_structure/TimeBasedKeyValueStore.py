"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store
"""
import collections

from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ''
        values = self.cache[key]
        idx = values.bisect(timestamp)
        if not idx:
            return ""
        return values.peekitem(idx - 1)[1]
