'''
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt_1 = collections.Counter(nums1)
        cnt_2 = collections.Counter(nums2)

        res = []
        for k, v in cnt_1.items():
            if not cnt_2[k]:
                continue
            res.extend([k] * min(cnt_2[k], v))

        return res


assert_value([2, 2], Solution().intersect, nums1=[1, 2, 2, 1], nums2=[2, 2])
assert_value([4, 9], Solution().intersect, nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
