'''
920. Number of Music Playlists
https://leetcode.com/problems/number-of-music-playlists/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0] * (goal + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * max(0, i - k)

        return dp[-1][-1] % (10 ** 9 + 7)


assert_value(6, Solution().numMusicPlaylists, n=3, goal=3, k=1)
assert_value(6, Solution().numMusicPlaylists, n=2, goal=3, k=0)
assert_value(2, Solution().numMusicPlaylists, n=2, goal=3, k=1)
