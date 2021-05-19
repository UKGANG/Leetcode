'''
470. Implement Rand10() Using Rand7()
https://leetcode.com/problems/implement-rand10-using-rand7/
'''
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40:
            result = (rand7() - 1) + (rand7() - 1) * 7

        return result % 10 + 1
