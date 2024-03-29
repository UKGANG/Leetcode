'''
935. Knight Dialer
https://leetcode.com/problems/knight-dialer/
'''

from test_tool import assert_value


class Solution:
    def knightDialer(self, n: int) -> int:
        jump_map = {
            0: {4, 6},
            1: {6, 8},
            2: {7, 9},
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {2, 4},
        }

        dp = [1] * 10

        for _ in range(n - 1):
            dp_next = [0] * 10
            for i in range(10):
                for j in jump_map[i]:
                    dp_next[i] += dp[j]
            dp = dp_next

        return sum(dp) % (10 ** 9 + 7)


assert_value(657107962, Solution().knightDialer, n=3130)
