'''
1762. Buildings With an Ocean View
https://leetcode.com/problems/buildings-with-an-ocean-view/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l = len(heights) - 1
        curr_top = 0
        res = []
        while l >= 0:
            if heights[l] > curr_top:
                res.append(l)
                curr_top = heights[l]
            l -= 1
        return res[::-1]


assert_value([0, 2, 3], Solution().findBuildings, heights=[4, 2, 3, 1])
assert_value([0, 1, 2, 3], Solution().findBuildings, heights=[4, 3, 2, 1])
assert_value([3], Solution().findBuildings, heights=[1, 3, 2, 4])
