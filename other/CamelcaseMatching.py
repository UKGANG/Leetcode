'''
1023. Camelcase Matching
https://leetcode.com/problems/camelcase-matching/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            p = 0
            for idx, c in enumerate(query):
                if p == len(pattern):
                    if not query[idx:].islower():
                        p += 1
                    break
                if c == pattern[p]:
                    p += 1
                elif c.isupper():
                    break
            res.append(p == len(pattern))
        return res


assert_value([True, False, True, True, False], Solution().camelMatch,
             queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB")
assert_value([True, False, True, False, False], Solution().camelMatch,
             queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa")
assert_value([False, True, False, False, False], Solution().camelMatch,
             queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBaT")
