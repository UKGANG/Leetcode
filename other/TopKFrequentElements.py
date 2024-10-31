'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
'''
import collections
import heapq
from typing import List

from test_tool import assert_value


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        pq = [(-v, k) for k, v in freq.items()]
        heapq.heapify(pq)
        res = []
        while k:
            res.append(heapq.heappop(pq)[1])
            k -= 1
        return res

    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        freq = sorted(freq.items(), key=lambda pair: -pair[1])[:k]
        return [k for k, v in freq]


assert_value([1, 2], Solution().topKFrequent, nums=[1, 1, 1, 2, 2, 3], k=2)
assert_value([1], Solution().topKFrequent, nums=[1], k=1)
