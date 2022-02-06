'''
478. Generate Random Point in a Circle
https://leetcode.com/problems/generate-random-point-in-a-circle/
'''
from math import pi, sqrt, cos, sin
from random import uniform
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self._r = radius
        self._x = x_center
        self._y = y_center

    def randPoint(self) -> List[float]:
        r = self._r * sqrt(uniform(0, 1))
        theta = uniform(0, 2 * pi)
        return [self._x + r * cos(theta), self._y + r * sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
