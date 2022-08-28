'''
860. Lemonade Change
https://leetcode.com/problems/lemonade-change/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cache = collections.Counter()
        for bill in bills:
            if bill == 5:
                cache[5] += 1
            elif bill == 10:
                if not cache[5]:
                    return False
                cache[5] -= 1
                cache[10] += 1
            elif bill == 20:
                if cache[10] and cache[5]:
                    cache[5] -= 1
                    cache[10] -= 1
                elif cache[5] > 2:
                    cache[5] -= 3
                else:
                    return False

        return True
