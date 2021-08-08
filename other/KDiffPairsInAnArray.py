'''
532. K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        res = set()
        for num in nums:
            if num - k in visited:
                res.add((num, num - k))
            if num + k in visited:
                res.add((num + k, num))
            visited.add(num)
        return len(res)

    def _findPairs(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        res = 0

        while counter:
            n1 = next(iter(counter))
            if k == 0:
                if counter[n1] > 1:
                    res += 1
            else:
                if n1 + k in counter:
                    res += 1
                if n1 - k in counter:
                    res += 1
            del counter[n1]
        return res


assert_value(2, Solution().findPairs, nums=[3, 1, 4, 1, 5], k=2)
assert_value(4, Solution().findPairs, nums=[1, 2, 3, 4, 5], k=1)
assert_value(1, Solution().findPairs, nums=[1, 3, 1, 5, 4], k=0)
