'''
2158. Amount of New Area Painted Each Day
https://leetcode.com/problems/amount-of-new-area-painted-each-day/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        painted = {}
        for i, j in paint:
            area = 0
            while j > i:
                if i in painted:
                    i = painted[i]
                else:
                    painted[i] = j
                    area += 1
                    i += 1
            res.append(area)
        return res


assert_value([3, 3, 1], Solution().amountPainted, paint=[[1, 4], [4, 7], [5, 8]])
assert_value([3, 3, 1], Solution().amountPainted, paint=[[1, 4], [5, 8], [4, 7]])
assert_value([4, 0], Solution().amountPainted, paint=[[1, 5], [2, 4]])
