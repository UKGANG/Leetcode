'''
373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
'''
from heapq import heappush, heappop
from typing import List

from test_tool import assert_value


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []

        for i in nums1:
            for j in nums2:
                if len(h) < k:
                    heappush(h, (-i - j, i, j))
                    continue
                if h[0][0] < -i - j:
                    heappop(h)
                    heappush(h, (-i - j, i, j))

        return sorted([[i, j] for k, i, j in h])


assert_value([[1, 2], [1, 4], [1, 6]], Solution().kSmallestPairs, nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
assert_value([[1, 1], [1, 1]], Solution().kSmallestPairs, nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
assert_value([[1, 3], [2, 3]], Solution().kSmallestPairs, nums1=[1, 2], nums2=[3], k=3)
