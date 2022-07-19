'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


assert_value([2], Solution().intersection, nums1=[1, 2, 2, 1], nums2=[2, 2])
assert_value([9, 4], Solution().intersection, nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
