"""
43. Multiply Strings
https://leetcode.com/problems/multiply-strings
"""
import itertools


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' == num1 or '0' == num2:
            return '0'
        if len(num1) > len(num2):
            return self.multiply(num2, num1)
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for x, y in itertools.product(range(len(num1)), range(len(num2))):
            carry = res[x + y]
            v1 = int(num1[x])
            v2 = int(num2[y])
            carry, v = divmod(v1 * v2 + carry, 10)
            res[x + y] = v
            res[x + y + 1] += carry

        if not res[-1]:
            res.pop()
        return ''.join([str(n) for n in reversed(res)])
