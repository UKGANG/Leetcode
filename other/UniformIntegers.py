'''
Uniform Integers
https://leetcode.com/discuss/interview-question/1555073/Facebook-or-Phone-or-Count-uniform-numbers-in-range
'''

from test_tool import assert_value


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    first_dig_n = len(str(A))
    first_dig_high = int(str(A)[0])
    last_dig_n = len(str(B))
    last_dig_high = int(str(B)[0])

    res = 0
    res += 1 if A <= int('1' * first_dig_n) * first_dig_high <= B else 0
    res += 1 if A <= int('1' * last_dig_n) * last_dig_high <= B else 0

    if last_dig_n - first_dig_n == 0:
        return res + last_dig_high - first_dig_high - 1

    res += (9 - first_dig_high)
    res += (last_dig_high - 1)

    res += ((last_dig_n - first_dig_n - 1) * 9)

    return res


assert_value(5, getUniformIntegerCountInInterval, A=75, B=300)
assert_value(9, getUniformIntegerCountInInterval, A=1, B=9)
assert_value(1, getUniformIntegerCountInInterval, A=999999999999, B=999999999999)
