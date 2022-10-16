'''
315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
'''
import bisect
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        seen = []
        res = []
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            res.append(bisect.bisect_left(seen, num))
            bisect.insort(seen, num)
        return res[::-1]
