'''
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
'''
from typing import List, NoReturn

from test_tool import assert_value


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s = self.removeSpace(s)
        l, r = 0, len(s) - 1
        self.swap(s, l, r)
        l = 0
        for r in range(len(s)):
            if s[r] == ' ':
                self.swap(s, l, r - 1)
                l = r + 1
            elif r == len(s) - 1:
                self.swap(s, l, r)

        return ''.join(s)

    def swap(self, s: List[str], l, r) -> NoReturn:
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def removeSpace(self, s: List[str]) -> List[str]:
        l, r, prev = 0, 0, None
        cnt = 0
        while r < len(s):
            if s[r] == ' ' and (r == 0 or prev == ' '):
                prev = ' '
                r += 1
                continue
            prev = s[r]
            cnt += 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r += 1
        if s[cnt - 1] == ' ':
            cnt -= 1
        return s[: cnt]


assert_value("blue is sky the", Solution().reverseWords, s="the sky is blue")
assert_value("world hello", Solution().reverseWords, s="  hello world  ")
assert_value("example good a", Solution().reverseWords, s="a good   example")
