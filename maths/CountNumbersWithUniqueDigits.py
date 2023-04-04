"""
357. Count Numbers with Unique Digits
https://leetcode.com/problems/count-numbers-with-unique-digits
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1

        res = 10
        unique_cnt = 9

        for i in range(2, min(n + 1, 11)):
            unique_cnt *= (9 - i + 2)
            res += unique_cnt

        return res
