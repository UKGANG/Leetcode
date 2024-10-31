'''
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/
'''
import bisect
import random
from typing import List

from test_tool import assert_value


class Solution:

    def __init__(self, w: List[int]):
        self._presum = w
        for i in range(1, len(w)):
            w[i] += w[i-1]

    def pickIndex(self) -> int:
        n = random.randint(1, self._presum[-1])
        return bisect.bisect_left(self._presum, n)

# Your Solution object will be instantiated and called as such:
obj = Solution([1, 3])
param_1 = obj.pickIndex()
param_2 = obj.pickIndex()