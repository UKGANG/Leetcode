'''
Count Maximum Teams
https://leetcode.com/discuss/interview-question/1594880/Amazon-OA-questions-countMaximumTeams
'''
from typing import List

from test_tool import assert_value


class Solution:
    def countMaximumTeams(self, skill: List[int], size: int, diff: int) -> int:
        answer = 0

        skill.sort()

        i = 0
        while (i <= (len(skill) - size)):
            if (skill[i + size - 1] - skill[i] <= diff):
                answer += 1
                i += size
            else:
                i += 1
        return answer


assert_value(2, Solution().countMaximumTeams, skill=[3, 4, 3, 1, 6, 5], size=3, diff=2)
