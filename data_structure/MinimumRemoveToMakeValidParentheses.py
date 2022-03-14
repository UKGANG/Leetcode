'''
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''

from test_tool import assert_value


class Solution:
    def minRemoveToMakeValid_v1(self, s: str) -> str:
        res = ''
        stack = []
        for c in s:
            if c == '(':
                stack.append(res)
                res = ''
                continue
            if c == ')':
                if not stack:
                    continue
                res = f'({res})'
                res = f'{stack.pop()}{res}'
                continue
            res = f'{res}{c}'

        stack.append(res)
        return ''.join(stack)

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                if stack:
                    curr = stack.pop() + f'({curr})'
            else:
                curr = curr + c
        while stack:
            curr = stack.pop() + curr
        return ''.join(curr)


assert_value("lee(t(c)o)de", Solution().minRemoveToMakeValid, s="lee(t(c)o)de)")
assert_value("ab(c)d", Solution().minRemoveToMakeValid, s="a)b(c)d")
assert_value("", Solution().minRemoveToMakeValid, s="))((")
assert_value("()()", Solution().minRemoveToMakeValid, s="())()(((")
