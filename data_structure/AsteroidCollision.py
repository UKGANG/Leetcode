"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/
"""
from typing import List

from test_tool import assert_value


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            while stack:
                right_asteroid = stack.pop()
                if right_asteroid + asteroid < 0:
                    continue
                elif right_asteroid + asteroid > 0:
                    stack.append(right_asteroid)
                asteroid = 0
                break
            if asteroid:
                res.append(asteroid)
        res.extend(stack)
        return res
