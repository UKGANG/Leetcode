'''
460. LFU Cache
https://leetcode.com/problems/lfu-cache/
'''
import collections
from typing import List

from test_tool import assert_value


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._min_freq = 0
        self._key_freq = {}
        self._freq_key = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self._key_freq:
            return -1
        freq = self._key_freq[key]

        val = self._freq_key[freq][key]
        del self._freq_key[freq][key]
        if not self._freq_key[freq]:
            if freq == self._min_freq:
                self._min_freq += 1
            del self._freq_key[freq]
        self._freq_key[freq + 1][key] = val
        self._key_freq[key] += 1

        return val

    def put(self, key: int, value: int) -> None:
        if not self._capacity:
            return
        if key in self._key_freq:
            freq = self._key_freq[key]
            self._freq_key[freq][key] = value
            self.get(key)
            return

        if self._capacity == len(self._key_freq):
            # remove a key
            min_key, min_val = self._freq_key[self._min_freq].popitem(last=False)
            del self._key_freq[min_key]

        self._key_freq[key] = 1
        self._freq_key[1][key] = value
        self._min_freq = 1


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
param_1 = obj.get(1)
print(param_1)
obj.put(1, 2)
obj.put(2, 4)
param_1 = obj.get(1)
print(param_1)
param_2 = obj.get(2)
print(param_2)
