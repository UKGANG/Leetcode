'''
1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
follow up: what if there is a weighted skill k = [1,-1,3] 具体描述不太记得了
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxScore(self, cardPoints: List[int], k: int, weights: List[int]) -> int:
        res = float('-inf')
        for i in range(k + 1):
            left = cardPoints[:k - i] if k - i else []
            right = cardPoints[-i:] if -i else []
            curr = self.get_weighted_sum(left, right[::-1], weights)
            res = max(res, curr)
        return res

    def get_weighted_sum(self, left: List[int], right: List[int], weight: List[int]) -> int:
        dp = [None] * (len(left) + 1)
        for i in range(len(dp)):
            dp[i] = [0] * (len(right) + 1)
        for i in range(1, len(left) + 1):
            dp[i][0] = dp[i - 1][0] + left[i - 1] * weight[i - 1]

        for i in range(1, len(right) + 1):
            dp[0][i] = dp[0][i - 1] + right[i - 1] * weight[i - 1]

        for i in range(1, len(left) + 1):
            for j in range(1, len(right) + 1):
                dp[i][j] = max(
                    dp[i - 1][j] + left[i - 1] * weight[i + j - 1],
                    dp[i][j - 1] + right[j - 1] * weight[i + j - 1],
                )
        return dp[-1][-1]


assert_value(12, Solution().maxScore, cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3, weights=[1, 2, 3])
