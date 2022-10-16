'''
493. Reverse Pairs
https://leetcode.com/problems/reverse-pairs/
'''
import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        seen = []
        res = 0
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            res += bisect.bisect_left(seen, num)
            bisect.insort(seen, num << 1)
        return res
