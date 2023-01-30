'''
1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [
            [0] * (n + 1) for _ in range(m + 1)
        ]

        nums1.insert(0, -1)
        nums2.insert(0, -1)

        for x, y in itertools.product(range(1, m + 1), range(1, n + 1)):
            if nums1[x] != nums2[y]:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1])
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1] + 1)
        return dp[-1][-1]

    def _maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        nums1.insert(0, None)
        nums2.insert(0, None)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i] != nums2[j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        return max(sum(dp, []))


assert_value(2, Solution().maxUncrossedLines, nums1=[1, 4, 2], nums2=[1, 2, 4])
assert_value(2, Solution().maxUncrossedLines, nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1])
