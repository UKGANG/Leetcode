'''
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/
'''
import math
import re
from typing import List

from test_tool import assert_value


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        first_negative = False
        if s[0] == '-':
            first_negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        nums = re.split('[\+\-\*\/]', s)
        nums[0] = int(nums[0])
        if first_negative:
            nums[0] = -nums[0]

        ops = [op for op in re.split('\d', s) if op]

        result = [nums[0]]
        nums = nums[1:]
        for idx in range(len(nums)):
            op = ops[idx]
            num = int(nums[idx])
            if op == '*':
                result[-1] *= num
            elif op == '/':
                result[-1] = result[-1] / num
                result[-1] = math.floor(result[-1]) if result[-1] > 0 else math.ceil(result[-1])
            elif op == '+':
                result.append(num)
            else:
                result.append(-num)

        return math.floor(sum(result))


assert_value(7, Solution().calculate, s="3+2*2")
assert_value(1, Solution().calculate, s=" 3/2 ")
assert_value(5, Solution().calculate, s=" 3+5 / 2 ")
assert_value(8, Solution().calculate, s="14/3*2")
assert_value(13, Solution().calculate, s="14-3/2")
