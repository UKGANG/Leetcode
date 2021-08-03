'''
Secret Array
https://leetcode.com/discuss/interview-question/1332322/amazon-online-assessment-july-2021-secret-array
'''
from typing import List

from test_tool import assert_value


class Solution:
    def countAnalogousArrays(self, consecutiveDifference, lowerBound, upperBound):
        # Write your code here
        # Find the maximum difference in the sequence
        upper_diff = 0
        lower_diff = 0
        curr_diff = 0
        for diff in consecutiveDifference:
            curr_diff += diff
            upper_diff = max(upper_diff, curr_diff)
            lower_diff = min(lower_diff, curr_diff)
        range_diff = upper_diff - lower_diff

        return max(0, upperBound - lowerBound - range_diff + 1)
