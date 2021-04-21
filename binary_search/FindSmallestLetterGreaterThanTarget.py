'''
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)
        if target < ord(letters[0]) or target >= ord(letters[-1]):
            return letters[0]

        l, r = 0, len(letters)
        while l < r:
            m = (l + r) >> 1
            if ord(letters[m]) <= target:
                l = m + 1
            else:
                r = m

        return letters[l]


assert_value("c", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="a")
assert_value("f", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="c")
assert_value("f", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="d")
assert_value("j", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="g")
assert_value("c", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="j")
assert_value("c", Solution().nextGreatestLetter, letters=["c", "f", "j"], target="k")
assert_value("v", Solution().nextGreatestLetter, letters=["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], target="q")
