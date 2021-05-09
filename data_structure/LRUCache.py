'''
146. LRU Cache
https://leetcode.com/problems/lru-cache/
'''
from collections import defaultdict, OrderedDict
from test_tool import assert_value


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self._cache and len(self._cache) >= self._capacity:
            self._cache.popitem(last=False)

        self._cache[key] = value
        self._cache.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
assert_value(1, obj.get, key=1)
obj.put(3, 3)
assert_value(-1, obj.get, key=2)
obj.put(4, 4)
assert_value(-1, obj.get, key=1)
assert_value(3, obj.get, key=3)
assert_value(4, obj.get, key=4)
