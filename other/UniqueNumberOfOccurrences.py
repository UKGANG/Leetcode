'''
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        res = collections.Counter(cnt.values())
        return len(cnt) == len(res)


assert_value(True, Solution().uniqueOccurrences, arr=[1, 2, 2, 1, 1, 3])
assert_value(False, Solution().uniqueOccurrences, arr=[1, 2])
assert_value(True, Solution().uniqueOccurrences, arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
