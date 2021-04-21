'''
1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mapping = {}
        for e in arr:
            mapping[e] = 1 if e not in mapping else 1 + mapping[e]
        mapping = dict(sorted(mapping.items(), key=lambda e: e[1], reverse=True))
        size = len(arr)
        value = [v for k, v in mapping.items()]
        cnt = 0
        res = size
        for v in value:
            cnt += 1
            res -= v
            if size >= res * 2:
                break
        return cnt


assert_value(2, Solution().minSetSize, arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
assert_value(1, Solution().minSetSize, arr=[7, 7, 7, 7, 7, 7])
assert_value(1, Solution().minSetSize, arr=[1, 9])
assert_value(1, Solution().minSetSize, arr=[1000, 1000, 3, 7])
assert_value(5, Solution().minSetSize, arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
