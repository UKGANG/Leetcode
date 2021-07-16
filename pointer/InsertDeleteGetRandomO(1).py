'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
import random
from typing import List

from test_tool import assert_value


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list_cache = []
        self._idx_cache = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._idx_cache:
            return False

        self._list_cache.append(val)
        self._idx_cache[val] = len(self._list_cache) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._idx_cache:
            return False

        self._list_cache[self._idx_cache[val]] = self._list_cache[-1]
        self._idx_cache[self._list_cache[-1]] = self._idx_cache[val]
        del self._list_cache[-1]
        del self._idx_cache[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._list_cache)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# assert_value(True, obj.insert, val=1)
# assert_value(False, obj.remove, val=2)
# assert_value(True, obj.insert, val=2)
# assert obj.getRandom() in [1, 2]
# assert_value(True, obj.remove, val=1)
# assert_value(False, obj.insert, val=2)
# assert_value(2, obj.getRandom)

obj = RandomizedSet()
assert_value(True, obj.insert, val=0)
assert_value(True, obj.insert, val=1)
assert_value(True, obj.remove, val=0)
assert_value(True, obj.insert, val=2)
assert_value(True, obj.remove, val=1)
assert_value(2, obj.getRandom)
