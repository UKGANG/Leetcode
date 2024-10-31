"""
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections
"""
from typing import List

from test_tool import assert_value


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx_1 = idx_2 = 0
        m, n = len(firstList), len(secondList)
        res = []
        while idx_1 < m and idx_2 < n:
            # Make sure the pointer to the firstList always start before the secondList
            if firstList[idx_1][0] > secondList[idx_2][0]:
                firstList, secondList = secondList, firstList
                idx_1, idx_2 = idx_2, idx_1
                m, n = n, m

            if firstList[idx_1][-1] >= secondList[idx_2][0]:
                # overlapping
                res.append([secondList[idx_2][0], min(firstList[idx_1][-1], secondList[idx_2][-1])])

            if firstList[idx_1][-1] > secondList[idx_2][-1]:
                idx_2 += 1
            else:
                idx_1 += 1

        return res
