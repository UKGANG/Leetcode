'''
818. Race Car
https://leetcode.com/problems/race-car/
'''
import collections
import math
from typing import List

from test_tool import assert_value


class Solution:
    def racecar(self, target: int) -> int:
        def dfs(dist):
            if dist in dp:
                return dp[dist]

            n = math.ceil(math.log(dist + 1, 2))
            if 1 << n == dist + 1:
                dp[dist] = n
            else:
                dp[dist] = n + 1 + dfs((1 << n) - 1 - dist)
                for i in range(n):
                    dp[dist] = min(dp[dist], n + 1 + i + dfs(dist - (1 << (n - 1)) + (1 << i)))
            return dp[dist]

        dp = {}
        dfs(target)

        return dp[target]

    def __racecar(self, target: int) -> int:
        seen = set((0, 1))

        queue = collections.deque([(0, 1)])

        cnt = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pos, speed = queue.popleft()
                if (pos, speed) in seen:
                    continue
                seen.add((pos, speed))
                if pos == target:
                    return cnt
                queue.append((pos, -1 if speed > 0 else 1))
                pos += speed
                speed <<= 1
                queue.append((pos, speed))
            cnt += 1
        return -1

    def __init__(self):
        self.dp = {}

    def _racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]

        n = math.ceil(math.log(target + 1, 2))
        if 1 << n == target + 1:
            self.dp[target] = n
        else:
            self.dp[target] = n + self._racecar((1 << n) - 1 - target) + 1
            for i in range(n):
                self.dp[target] = min(self.dp[target], n + self._racecar(target - (1 << (n - 1)) + (1 << i)) + 1 + i)
        return self.dp[target]


assert_value(2, Solution().racecar, target=3)
assert_value(5, Solution().racecar, target=6)
assert_value(7, Solution().racecar, target=5)
assert_value(5, Solution().racecar, target=4)
