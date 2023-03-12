"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        smallest = -1
        for i in range(len(s) - 1, -1, -1):
            curr = mapping[s[i]]
            if curr < smallest:
                res -= curr
            else:
                res += curr
                smallest = curr
        return res
