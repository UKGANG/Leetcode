'''
1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxScore_loop(self, cardPoints: List[int], k: int) -> int:
        curr = res = sum(cardPoints[:k])
        for i in range(k):
            curr = curr - cardPoints[k - 1 - i] + cardPoints[-i - 1]
            res = max(res, curr)
        return res

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return self.maxScore_loop(cardPoints, k)


assert_value(12, Solution().maxScore, cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3)
