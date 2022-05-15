'''
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/
'''
from typing import List

from test_tool import assert_value


class Solution:
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
