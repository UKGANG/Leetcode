'''
Balance Brackets
'''
import collections

from test_tool import assert_value


def isBalanced(s):
    cache = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = []
    for c in s:
        if c in cache:
            stack.append(c)
        else:
            if len(stack) == 0 or c != cache[stack.pop()]:
                return False
    return len(stack) == 0


assert_value(True, isBalanced, s='{[()]}')
assert_value(True, isBalanced, s='{}()')
assert_value(False, isBalanced, s='{(})')
assert_value(False, isBalanced, s=')')
