'''
Caesar Cipher
https://www.hackerrank.com/challenges/caesar-cipher-1/problem
'''
from typing import List

from test_tool import assert_value


def caesarCipher(s, k):
    base_cache = {
        1: ord('a'),
        0: ord('A'),
        -1: 0
    }
    mark = [1 if c.islower() else 0 if c.isupper() else -1 for c in s]
    s = [ord(c) - base_cache[m] for c, m in zip(s, mark)]
    s = [(n + k) % 26 if m != -1 else n for n, m in zip(s, mark)]
    s = [chr(n + base_cache[m]) for n, m in zip(s, mark)]

    return ''.join(s)


assert_value('okffng-Qwvb', caesarCipher, s='middle-Outz', k=2)
