'''
2007. Find Original Array From Doubled Array
https://leetcode.com/problems/find-original-array-from-doubled-array/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        counter = collections.Counter(changed)
        res = []
        for key in counter.keys():
            if key == 0:
                if counter[key] & 1:
                    return []
                res += [0] * (counter[0] >> 1)
                continue
            if not counter[key]:
                continue
            x = key
            while x & 1 == 0 and counter[x >> 1]:
                x >>= 1

            while x in counter:
                if counter[x]:
                    if counter[x] > counter[x << 1]:
                        return []
                    res += [x] * counter[x]
                    counter[x << 1] -= counter[x]
                    counter[x] = 0
                x <<= 1

        return res

    def _findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if len(changed) & 1:
            return []

        changed = sorted(changed)
        cache = collections.defaultdict(list)
        for idx, num in enumerate(changed):
            cache[num].append(idx)
        res = []
        idx = 0
        while idx < n:
            curr = changed[n - 1 - idx]
            idx += 1
            if curr not in cache:
                continue
            if curr & 1 == 1:
                return []
            if curr >> 1 not in cache:
                return []

            del cache[curr][-1]
            del cache[curr >> 1][-1]
            if len(cache[curr]) == 0:
                del cache[curr]
            if len(cache[curr >> 1]) == 0:
                del cache[curr >> 1]
            res.append(curr >> 1)

        return sorted(res)


assert_value([1, 3, 4], Solution().findOriginalArray, changed=[1, 3, 4, 2, 6, 8])
assert_value([], Solution().findOriginalArray, changed=[6, 3, 0, 1])
assert_value([], Solution().findOriginalArray, changed=[1])
assert_value([0, 0], Solution().findOriginalArray, changed=[0, 0, 0, 0])
assert_value([1], Solution().findOriginalArray, changed=[2, 1])
