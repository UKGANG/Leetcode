'''
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 4:
            if len(arr) < 3:
                return arr[0]
            if arr[0] == arr[1]:
                return arr[0]
            return arr[1]

        quarter = int(len(arr) / 4)
        step = quarter * 2
        for i in range(quarter, len(arr), step):
            l = r = i
            while l > -1 and arr[l] == arr[i]:
                l -= 1
            l += 1
            while r < len(arr) and arr[r] == arr[i]:
                r += 1
            r -= 1
            if r - l < quarter:
                continue
            return arr[i]
        return arr[step]


assert_value(6, Solution().findSpecialInteger, arr=[1, 2, 2, 6, 6, 6, 6, 7, 10])
assert_value(1, Solution().findSpecialInteger, arr=[1, 1])
assert_value(1, Solution().findSpecialInteger, arr=[1, 1, 1, 1])
