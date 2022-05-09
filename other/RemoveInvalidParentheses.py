'''
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        q = set([s])
        while True:
            [res.add(e) for e in q if self.valid(e)]
            if res:
                return sorted(list(res))
            q_next = set()
            for s in q:
                for j in range(len(s)):
                    if s[j] not in '()':
                        continue
                    q_next.add(f'{s[:j]}{s[j + 1:]}')
            q = q_next

        return []

    def valid(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False

        return not cnt


assert_value(["(())()", "()()()"], Solution().removeInvalidParentheses, s="()())()")
assert_value(["(a())()", "(a)()()"], Solution().removeInvalidParentheses, s="(a)())()")
assert_value([""], Solution().removeInvalidParentheses, s=")(")
