"""
1386. Cinema Seat Allocation
https://leetcode.com/problems/cinema-seat-allocation
"""
import collections
import operator
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def convert_to_bit(bookings):
            res = 0
            for booking in bookings:
                res |= (1 << booking)
            return res

        groups = collections.Counter()
        reservedSeats.sort(key=operator.itemgetter(1))
        for row, col in reservedSeats:
            if col in [1, 10]:
                continue
            groups[row] |= (1 << col)

        res = 0
        for bit_mask in groups.values():
            if (bit_mask & convert_to_bit([2, 3, 4, 5])) == 0:
                res += 1
                continue
            if (bit_mask & convert_to_bit([4, 5, 6, 7])) == 0:
                res += 1
                continue
            if (bit_mask & convert_to_bit([6, 7, 8, 9])) == 0:
                res += 1
                continue

        return res + ((n - len(groups)) << 1)
