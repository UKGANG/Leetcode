'''
202. Happy Number
https://leetcode.com/problems/happy-number/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        n: str = str(n)
        while n not in cache:
            cache.add(n)
            n: int = sum(int(c) ** 2 for c in n)
            n: str = str(n)
            if n == '1':
                return True
        return False


assert_value(True, Solution().isHappy, n=19)
assert_value(False, Solution().isHappy, n=2)
assert_value(True, Solution().isHappy, n=7)
