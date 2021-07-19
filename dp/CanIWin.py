'''
464. Can I Win
https://leetcode.com/problems/can-i-win/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        options = [i for i in range(1, maxChoosableInteger + 1)]
        options = tuple(options)
        if sum(options) < desiredTotal:
            return False
        return self.check_case(options, desiredTotal, 0, {})

    def check_case(self, options: tuple, desiredTotal: int, currentTotal: int, cache: dict):
        if options in cache:
            return cache[options]
        else:
            cache[options] = False
            if max(options) + currentTotal >= desiredTotal:
                cache[options] = True
            elif options:
                for i, opt in enumerate(options):
                    options_new = (*options[:i], *options[i + 1:])
                    if not self.check_case(options_new, desiredTotal, currentTotal + opt, cache):
                        cache[options] = True
                        break
            return cache[options]


assert_value(False, Solution().canIWin, maxChoosableInteger=10, desiredTotal=11)
assert_value(True, Solution().canIWin, maxChoosableInteger=10, desiredTotal=0)
assert_value(True, Solution().canIWin, maxChoosableInteger=10, desiredTotal=1)
