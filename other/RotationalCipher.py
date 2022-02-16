'''
Rotational Cipher
https://kristinelpetrosyan.medium.com/facebook-interview-question-rotational-cipher-b20337ca5c8
'''
from typing import List

from test_tool import assert_value


def rotationalCipher(input, rotation_factor):
    # Write your code here
    res = []
    for c in input:
        if c.isnumeric():
            c = convert_numeric(c, rotation_factor)
        elif c.isalpha():
            c = convert_alpha(c, rotation_factor)
        else:
            c = convert_others(c)
        res.append(c)

    return "".join(res)


def convert_numeric(c: str, rotation_factor: int) -> str:
    return str((int(c) + rotation_factor) % 10)


def convert_alpha(c: str, rotation_factor: int) -> str:
    base_lower = ord('a')
    base_upper = ord('A')
    base = base_upper if c.isupper() else base_lower
    n = ord(c) - base
    n = (n + rotation_factor) % 26 + base
    return chr(n)


def convert_others(c: str) -> str:
    return c


assert_value('Cheud-726?', rotationalCipher, input='Zebra-493?', rotation_factor=3)
assert_value('nopqrstuvwxyzABCDEFGHIJKLM9012345678', rotationalCipher, input='abcdefghijklmNOPQRSTUVWXYZ0123456789',
             rotation_factor=39)
