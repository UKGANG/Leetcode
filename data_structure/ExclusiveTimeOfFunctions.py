'''
636. Exclusive Time of Functions
https://leetcode.com/problems/exclusive-time-of-functions/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        idx = 0
        while idx < len(logs):
            idx_2, opt_2, t_2 = logs[idx].split(":")
            idx_2, t_2 = int(idx_2), int(t_2)
            if 'start' == opt_2:
                stack.append((idx_2, t_2))
            else:
                idx_1, t_1 = stack.pop()
                time_cost = t_2 - t_1 + 1
                res[idx_1] += time_cost
                if stack:
                    idx_recursion = stack[-1][0]
                    res[idx_recursion] -= time_cost
            idx += 1

        return res


assert_value([3, 4], Solution().exclusiveTime, n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
assert_value([8], Solution().exclusiveTime, n=1,
             logs=["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"])
assert_value([7, 1], Solution().exclusiveTime, n=2,
             logs=["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"])
assert_value([8, 1], Solution().exclusiveTime, n=2,
             logs=["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"])
assert_value([1], Solution().exclusiveTime, n=1, logs=["0:start:0", "0:end:0"])
