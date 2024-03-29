"""
276. Paint Fence
https://leetcode.com/problems/paint-fence
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        dp = [0] * n

        dp[0] = k
        dp[1] = k * k

        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)

        return dp[n - 1]
