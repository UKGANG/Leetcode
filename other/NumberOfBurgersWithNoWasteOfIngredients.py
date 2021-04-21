'''
1276. Number of Burgers with No Waste of Ingredients
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2

        if not x.is_integer() or not y.is_integer():
            return []
        if x < 0 or y < 0:
            return []

        return [int(x), int(y)]


assert_value([1, 6], Solution().numOfBurgers, tomatoSlices=16, cheeseSlices=7)
assert_value([], Solution().numOfBurgers, tomatoSlices=17, cheeseSlices=4)
assert_value([], Solution().numOfBurgers, tomatoSlices=4, cheeseSlices=17)
assert_value([0, 0], Solution().numOfBurgers, tomatoSlices=0, cheeseSlices=0)
assert_value([0, 1], Solution().numOfBurgers, tomatoSlices=2, cheeseSlices=1)
