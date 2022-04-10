'''
158. Read N Characters Given read4 II - Call Multiple Times
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
'''
from typing import List

from test_tool import assert_value


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self._inner_buffer = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        res = 0
        offset = 0
        while self._inner_buffer and n:
            buf[offset] = self._inner_buffer.popleft()
            offset += 1
            res += 1
            n -= 1

        while n:
            buf4 = [None] * 4
            read4(buf4)

            for i in range(n, 4):
                if buf4[i] is None:
                    break
                self._inner_buffer.append(buf4[i])

            for i in range(min(n, 4)):
                if buf4[i] is None:
                    return res
                buf[offset] = buf4[i]
                offset += 1
                res += 1
                n -= 1

        return res