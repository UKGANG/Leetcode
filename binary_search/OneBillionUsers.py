'''
1 Billion Users
https://leetcode.com/discuss/interview-question/746520/facebook-recruiting-portal-1-billion-users
'''
from typing import List

from test_tool import assert_value


def getBillionUsersDay(growthRates):
    # Write your code here
    upper_bound = 1
    while True:
        n = sum([rate ** upper_bound for rate in growthRates])
        if n >= 1000000000:
            break
        upper_bound = upper_bound << 1

    l, r = upper_bound >> 1, upper_bound
    while l < r:
        m = (l + r) >> 1
        n = sum([rate ** m for rate in growthRates])
        if n < 1000000000:
            l = m + 1
        else:
            r = m
    return r


assert_value(52, getBillionUsersDay, growthRates=[1.5])
assert_value(79, getBillionUsersDay, growthRates=[1.1, 1.2, 1.3])
assert_value(1047, getBillionUsersDay, growthRates=[1.01, 1.02])
