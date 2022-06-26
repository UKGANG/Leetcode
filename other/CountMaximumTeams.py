'''
Count Maximum Teams
https://leetcode.com/discuss/interview-question/1594880/Amazon-OA-questions-countMaximumTeams
'''
from typing import List

from test_tool import assert_value


class Solution:
    def countMaximumTeams(self, skill: List[int], size: int, diff: int) -> int:
        idx = size
        res = 0
        skill = sorted(skill)
        while idx <= len(skill):
            if skill[idx - 1] - skill[idx - size] <= diff:
                res += 1
                idx += size
            else:
                idx += 1
        return res


# assert_value(2, Solution().countMaximumTeams, skill=[3, 4, 3, 1, 6, 5], size=3, diff=2)
# assert_value(2, Solution().countMaximumTeams, skill=[20, 22, 23, 14, 16, 15], size=3, diff=4)
assert_value(1, Solution().countMaximumTeams, skill=[10, 15, 9, 10, 9, 1, 3, 3], size=5, diff=2)
