"""
Set Selection
https://leetcode.com/discuss/interview-question/1917748/nordstrom-oa-2022-set-selection
"""
from typing import List
from test_tool import assert_value


class Solution:
    def selectSet(self, arr: List[List[int]]):
        groups = arr
        m = len(groups)
        n = len(groups[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 0
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(groups[i][j] - groups[i - 1][k]))
        min_dist = float('inf')
        last_point = -1
        for j in range(n):
            if dp[m - 1][j] < min_dist:
                min_dist = dp[m - 1][j]
                last_point = j
        points = [0] * m
        points[m - 1] = last_point
        for i in range(m - 2, -1, -1):
            min_dist = float('inf')
            prev_point = -1
            for j in range(n):
                if dp[i][j] + abs(groups[i][j] - groups[i + 1][last_point]) < min_dist:
                    min_dist = dp[i][j] + abs(groups[i][j] - groups[i + 1][last_point])
                    prev_point = j
            points[i] = prev_point
            last_point = prev_point
        return sorted(points)


assert_value([1, 3, 6], Solution().selectSet, arr=[
    [21, 1, 150, 289, -321],
    [160, 3, 30, ],
    [170, 22, 6, 7]

])
