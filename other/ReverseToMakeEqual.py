'''
1460. Make Two Arrays Equal by Reversing Sub-arrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target = sorted(target)
        arr = sorted(arr)
        return not bool(sum([abs(a - b) for a, b in zip(target, arr)]))


assert_value(True, Solution().canBeEqual, target=[1, 2, 3, 4], arr=[1, 4, 3, 2])
assert_value(False, Solution().canBeEqual, target=[1, 2, 3, 4], arr=[1, 2, 3, 5])
assert_value(False, Solution().canBeEqual, target=[1, 2, 3], arr=[2, 2, 2])
