'''
706. Design HashMap
https://leetcode.com/problems/design-hashmap/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


class MyHashMap:

    def __init__(self):
        self._cache = [None] * (10 ** 6)

    def put(self, key: int, value: int) -> None:
        self._cache[key - 1] = value

    def get(self, key: int) -> int:
        res = self._cache[key - 1]
        return -1 if res is None else res

    def remove(self, key: int) -> None:
        self._cache[key - 1] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
