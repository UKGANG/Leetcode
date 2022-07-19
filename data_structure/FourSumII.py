'''
454. 4Sum II
https://leetcode.com/problems/4sum-ii/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        cache_1 = collections.Counter(nums1)
        cache_2 = collections.Counter(nums2)
        cache_3 = collections.Counter(nums3)
        cache_4 = collections.Counter(nums4)

        cache_12 = collections.Counter()
        for a, b in itertools.product(
                cache_1.items(),
                cache_2.items(),
        ):
            cache_12[a[0] + b[0]] += a[1] * b[1]

        cache_34 = collections.Counter()
        for c, d in itertools.product(
                cache_3.items(),
                cache_4.items(),
        ):
            cache_34[c[0] + d[0]] += c[1] * d[1]

        for x, y in itertools.product(
                cache_12.items(),
                cache_34.items(),
        ):
            if x[0] + y[0] == 0:
                res += x[1] * y[1]
        return res


assert_value(2, Solution().fourSumCount, nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
assert_value(1, Solution().fourSumCount, nums1=[0], nums2=[0], nums3=[0], nums4=[0])
