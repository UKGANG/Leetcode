"""
Stock purchase

"""
from typing import List

from test_tool import assert_value


class Solution:
    def purchase(self, prices: List[int]):
        res = 0
        curr_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            curr_max = max(curr_max, prices[i])
            res += curr_max - prices[i]
        return res

    def _purchase(self, prices: List[int]):
        stack = []
        res = 0
        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] <= prices[i]:
                stack.pop()
            stack.append(prices[i])
            res += stack[0] - prices[i]
        return res


assert_value(12, Solution().purchase, prices=[3, 1, 7, 2, 4])
assert_value(8, Solution().purchase, prices=[-1, -1, 2, -1, 1])
