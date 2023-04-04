'''
Minimum Length Of The Roof
https://leetcode.com/discuss/interview-question/1317796/amazon-oa-2021-hackerrank
'''
from typing import List

from test_tool import assert_value


class Solution:
    def min_roof(self, parking_spot: List[int], k: int) -> int:
        res = float('inf')
        parking_spot.sort()

        # Sliding window, checking positions for k cars
        for i in range(k - 1, len(parking_spot)):
            window_start = parking_spot[i - k + 1]
            window_end = parking_spot[i]
            window_length = window_end - window_start
            window_length += 1
            res = min(res, window_length)

        return res


assert_value(3, Solution().min_roof, parking_spot=[2, 5, 6, 7], k=3)
assert_value(9, Solution().min_roof, parking_spot=[2, 10, 8, 17], k=3)
