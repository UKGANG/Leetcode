'''
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(i, curr, prev, exp, res):
            if i == len(num) and curr == target:
                res.append(''.join(exp))
                return
            for j in range(i + 1, len(num) + 1):
                if j > i + 1 and num[i] == '0':
                    break
                n = int(num[i:j])
                if i == 0:
                    exp.append(num[i:j])
                    backtrack(j, n, n, exp, res)
                    exp.pop()
                    continue
                exp.append('+')
                exp.append(num[i:j])
                backtrack(j, curr + n, n, exp, res)
                exp.pop()
                exp.pop()

                exp.append('-')
                exp.append(num[i:j])
                backtrack(j, curr - n, -n, exp, res)
                exp.pop()
                exp.pop()

                exp.append('*')
                exp.append(num[i:j])
                backtrack(j, curr - prev + prev * n, prev * n, exp, res)
                exp.pop()
                exp.pop()

        res = []
        exp = []
        backtrack(0, 0, 0, exp, res)
        return res

    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        curr_level = [('', num, 0, None)]
        while curr_level:
            expr, curr_suffix, curr, prev = curr_level.pop()
            if curr_suffix == '':
                if curr == target:
                    res.append(expr)
                continue
            for i in range(1, len(curr_suffix) + 1):
                if i > 1 and curr_suffix[0] == '0':
                    break
                next_prefix, next_suffix = curr_suffix[:i], curr_suffix[i:]
                next_prefix_int = int(next_prefix)
                if prev is None:
                    curr_level.append((next_prefix, next_suffix, next_prefix_int, next_prefix_int))
                else:
                    curr_level.append((f'{expr}+{next_prefix}', next_suffix, curr + next_prefix_int, next_prefix_int))
                    curr_level.append((f'{expr}-{next_prefix}', next_suffix, curr - next_prefix_int, -next_prefix_int))
                    curr_level.append((
                        f'{expr}*{next_prefix}', next_suffix, curr - prev + prev * next_prefix_int,
                        prev * next_prefix_int))

        return sorted(res)


assert_value(["1*2*3", "1+2+3"], Solution().addOperators, num="123", target=6)
assert_value(["2*3+2", "2+3*2"], Solution().addOperators, num="232", target=8)
assert_value([], Solution().addOperators, num="3456237490", target=9191)
assert_value(["2*3+2", "2+3*2"], Solution().addOperators, num="232", target=8)
assert_value(["1*0+5", "10-5"], Solution().addOperators, num="105", target=5)
