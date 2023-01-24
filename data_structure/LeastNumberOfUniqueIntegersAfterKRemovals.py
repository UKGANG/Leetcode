'''
1481. Least Number of Unique Integers after K Removals
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
'''
import collections
import operator
from typing import List

from test_tool import assert_value


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        res = 0
        for _, cnt in sorted(counter.items(), key=operator.itemgetter(1)):
            if cnt > k:
                res += 1
            k = max(0, k - cnt)

        return res

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cache = {}
        for e in arr:
            if e not in cache:
                cache[e] = 1
            else:
                cache[e] += 1
        for key, value in sorted(cache.items(), key=lambda item: item[1]):
            k -= value
            if k >= 0:
                del cache[key]
            else:
                break

        return len(cache.keys())


assert_value(1, Solution().findLeastNumOfUniqueInts, arr=[5, 5, 4], k=1)
assert_value(2, Solution().findLeastNumOfUniqueInts, arr=[4, 3, 1, 1, 3, 3, 2], k=3)
