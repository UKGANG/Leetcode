'''
394. Decode String
https://leetcode.com/problems/decode-string/
'''
from typing import List, Union

from test_tool import assert_value


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n, token = '', ''
        for c in s:
            if c == '[':
                stack.append((token, n))
                token, n = '', ''
            elif c == ']':
                token_prev, n_prev = stack.pop()
                token, n = token_prev + int(n_prev) * token, ''
            elif c.isnumeric():
                n += c
            else:
                token += c
        return token


assert_value("aaabcbc", Solution().decodeString, s="3[a]2[bc]")
assert_value("accaccacc", Solution().decodeString, s="3[a2[c]]")
assert_value("abcabccdcdcdef", Solution().decodeString, s="2[abc]3[cd]ef")
assert_value("leetcode" * 100, Solution().decodeString, s="100[leetcode]")
assert_value("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef", Solution().decodeString,
             s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
