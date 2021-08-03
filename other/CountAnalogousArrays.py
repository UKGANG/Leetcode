'''
CountAnalogousArrays

'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._prefix = '(['
        self._suffix_mapping = {
            ')': '(',
            ']': '[',
        }
        self._placeholder = '?'

    def fillMissingBrackets(self, s):
        # Write your code here
        res = 0
        left_cache = collections.Counter()
        right_cache = collections.Counter()
        # Initialize the right_cache first
        for i in range(len(s)):
            if s[i] in self._prefix or s[i] == self._placeholder:
                right_cache[s[i]] += 1
            else:
                right_cache[self._suffix_mapping[s[i]]] -= 1

        for i in range(len(s)):
            # Initialize the left_cache:
            if s[i] in self._prefix or s[i] == self._placeholder:
                left_cache[s[i]] += 1
            else:
                left_cache[self._suffix_mapping[s[i]]] -= 1

            # Adjust the right_cache on the current char(an reversed operation to the left_cache)
            if s[i] in self._prefix or s[i] == self._placeholder:
                right_cache[s[i]] -= 1
            else:
                right_cache[self._suffix_mapping[s[i]]] += 1
            # If valid for the left half
            if 0 < i < len(s) - 1 and self._check_substring(left_cache) and self._check_substring(right_cache):
                res += 1

        return res

    def _check_substring(self, cache):
        rest_question_mark = cache['?'] - abs(cache['(']) - abs(cache['['])
        if rest_question_mark < 0:
            return False
        return rest_question_mark & 1 == 0


assert_value(0, Solution().fillMissingBrackets, s="")
assert_value(5, Solution().fillMissingBrackets, s="))?)?)?))?())()(??(?((())(?)?())((((()(?")
assert_value(48, Solution().fillMissingBrackets,
             s="[[[[]??[][[[][][[]][]][[[?]]]]?[][[][]]][]][[]]][?[]][[[[[]]]]][][][[]]]]]][]]]][[[]]]][]]][[]]][?][][?[[[[[][[]][]][][[[[?[[][[?][[[]][[[][][[?[[]]?]]]]]]][[[]][]?[[")
