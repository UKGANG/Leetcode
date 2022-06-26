'''
Decode String Frequency
https://leetcode.com/discuss/interview-question/1010329/goldman-sachs-online-encode-string
'''
from typing import List

from test_tool import assert_value


class Solution:
    def frequencyCount(self, s: str) -> List[int]:
        res = [0] * 26
        if not s:
            return res
        a_offset = ord('a') - 1
        for i in range(10, 27):
            s = s.replace(str(i) + '#', chr(i + a_offset))
        for i in range(11):
            s = s.replace(str(i), chr(i + a_offset))

        idx = len(s) - 1
        while idx > -1:
            if s[idx] == ')':
                n = ''
                idx -= 1
                while s[idx] != '(':
                    n += s[idx]
                    idx -= 1
                n = int(''.join(f'{ord(c) - a_offset}' for c in n[::-1]))
                idx -= 1
            else:
                n = 1
            c = s[idx]
            res[ord(c) - a_offset - 1] += n
            idx -= 1

        return res


assert_value([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             Solution().frequencyCount, s='1226#24#')
assert_value([2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             Solution().frequencyCount, s="1(2)23(3)")
assert_value([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1],
             Solution().frequencyCount, s="23#(2)24#25#26#23#(3)")
