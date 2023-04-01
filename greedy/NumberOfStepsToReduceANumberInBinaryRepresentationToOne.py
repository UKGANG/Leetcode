"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
"""


class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        res = carry = 0

        for i in range(n - 1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                res += 2
            else:
                res += 1
        return res + carry
