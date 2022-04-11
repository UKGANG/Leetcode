'''
1146. Snapshot Array
https://leetcode.com/problems/snapshot-array/
'''
import bisect
from collections import OrderedDict
from typing import List, Optional

from test_tool import assert_value


class SnapshotArray:

    def __init__(self, length: int):
        self._snap_id = 0
        self._cache = {}
        for i in range(length):
            self._cache[i] = OrderedDict()
            self._cache[i][self._snap_id] = 0

    def set(self, index: int, val: int) -> None:
        self._cache[index][self._snap_id] = val

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self._cache[index]:
            keys = self._cache[index].keys()
            keys = list(keys)
            idx = bisect.bisect_left(keys, snap_id)
            idx = idx if len(keys) > idx else idx - 1
            if keys[idx] > snap_id:
                idx -= 1
            snap_id = keys[idx]
        return self._cache[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
obj.set(0, 6)
param_3 = obj.get(0, 0)

assert_value(5, obj.get, index=0, snap_id=0)

obj = SnapshotArray(3)
obj.set(1, 6)
param_2 = obj.snap()
param_3 = obj.snap()
obj.set(1, 19)
obj.set(0, 4)
param_4 = obj.get(2, 1)
param_5 = obj.get(2, 0)
param_6 = obj.get(0, 1)

assert_value(0, obj.get, index=0, snap_id=1)
