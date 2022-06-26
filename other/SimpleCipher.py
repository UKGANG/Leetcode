'''
Simple Cipher
https://algo.monster/problems/amazon-oa-simple-cipher
'''
from typing import List

from test_tool import assert_value


class Solution:
    def simple_cipher(self, encryped: str, k: int):
        offset = ord('A')
        res = ''
        for c in encryped:
            res += chr((ord(c) - offset + 26 - k) % 26 + offset)
        return res


assert_value('TRYME', Solution().simple_cipher, encryped='VTAOG', k=2)
