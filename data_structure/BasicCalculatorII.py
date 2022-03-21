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
        num = ''
        stack = []
        idx = 0
        while idx < len(s):
            c = s[idx]
            if s[idx].isnumeric():
                num += c
                idx += 1
                continue
            if num:
                stack.append(int(num))
            if c == '+':
                num = ''
                idx += 1
            elif c == '-':
                num = '-'
                idx += 1
            else:
                curr = stack.pop()
                idx += 1
                num = ''
                while idx < len(s) and s[idx].isnumeric():
                    num += s[idx]
                    idx += 1
                if c == '*':
                    curr *= int(num)
                else:
                    curr /= int(num)
                    curr = int(curr)
                num = ''
                stack.append(curr)
        if not num:
            num = '0'
        num = int(num)
        return sum(stack) + num

    def _calculate(self, s: str) -> int:
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
assert_value(1, Solution().calculate, s="1")
