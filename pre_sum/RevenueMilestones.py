'''
Revenue Milestones
https://leetcode.com/discuss/interview-question/1188322/facebook-recruiting-portal-revenue-milestones
'''
import bisect
from test_tool import assert_value


def getMilestoneDays(revenues, milestones):
    running_revenues = []
    curr = 0
    for m in revenues:
        curr += m
        running_revenues.append(curr)

    res = []
    for milestone in milestones:
        idx = bisect.bisect_left(running_revenues, milestone)
        res.append(idx + 1)
    return res


assert_value([4, 6, 10], getMilestoneDays, revenues=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
             milestones=[100, 200, 500])
assert_value([2, 4, 4, 5], getMilestoneDays, revenues=[100, 200, 300, 400, 500], milestones=[300, 800, 1000, 1400])
assert_value([2, 2, 3, 4, 5], getMilestoneDays, revenues=[700, 800, 600, 400, 600, 700],
             milestones=[800, 1000, 2100, 2200, 3100])
