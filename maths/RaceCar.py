'''
818. Race Car
https://leetcode.com/problems/race-car/
'''
import math
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self.dp = {}

    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]

        n = math.ceil(math.log(target + 1, 2))
        if 1 << n == target + 1:
            self.dp[target] = n
        else:
            self.dp[target] = n + self.racecar((1 << n) - 1 - target) + 1
            for i in range(n):
                self.dp[target] = min(self.dp[target], n + self.racecar(target - (1 << (n - 1)) + (1 << i)) + 1 + i)
        return self.dp[target]


assert_value(2, Solution().racecar, target=3)
assert_value(5, Solution().racecar, target=6)
assert_value(7, Solution().racecar, target=5)
assert_value(5, Solution().racecar, target=4)
