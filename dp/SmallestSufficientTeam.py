'''
1125. Smallest Sufficient Team
https://leetcode.com/problems/smallest-sufficient-team/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        group = set()
        roster = defaultdict(list)
        for idx, skills in enumerate(people):
            for skill in skills:
                roster[skill].append(idx)

        return list(self.helper(set(req_skills), people, roster, group))

    def helper(self, req_skills, people, roster, group):
        if not req_skills:
            return set()

        skill = list(req_skills)[0]
        min_combo = set()
        for person in roster[skill]:
            if person in group:
                continue

            combo = self.helper(req_skills - set(people[person]), people, roster, group | {person}) | {person}
            if not min_combo or len(min_combo) > len(combo):
                min_combo = combo

        return min_combo


assert_value([0, 2], Solution().smallestSufficientTeam,
             req_skills=["java", "nodejs", "reactjs"],
             people=[["java"], ["nodejs"], ["nodejs", "reactjs"]])
assert_value([1, 2], Solution().smallestSufficientTeam,
             req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
             people=[["algorithms", "math", "java"],
                     ["algorithms", "math", "reactjs"],
                     ["java", "csharp", "aws"],
                     ["reactjs", "csharp"],
                     ["csharp", "math"],
                     ["aws", "java"]])
