'''
Matching Pairs
https://leetcode.com/discuss/interview-question/632717/facebook-recruiting-portal-matching-pairs
'''
from typing import List

from test_tool import assert_value


def matching_pairs(s, t):
    # Write your code here
    diff = sum([int(c1 != c2) for c1, c2 in zip(s, t)])
    size = len(s)
    if diff == 0:
        return size - 2
    if diff == 1:
        return size - 1
    return size


assert_value(4, matching_pairs, s="abcd", t="adcb")
assert_value(1, matching_pairs, s="mno", t="mno")
assert_value(5, matching_pairs, s="abcde", t="adcbe")
assert_value(2, matching_pairs, s="abcd", t="abcd")
