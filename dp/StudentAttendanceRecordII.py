'''
552. Student Attendance Record II
https://leetcode.com/problems/student-attendance-record-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        mod = 10 ** 9 + 7
        dp = [1, 1, 2]
        for _ in range(2, n + 1):
            dp.append((dp[-1] + dp[-2] + dp[-3]) % mod)

        res = dp[-1]
        for i in range(1, n + 1):
            res += (dp[i] * dp[n - i + 1] % mod)
            res %= mod

        return res


assert_value(8, Solution().checkRecord, n=2)
assert_value(3, Solution().checkRecord, n=1)
assert_value(19, Solution().checkRecord, n=3)
assert_value(183236316, Solution().checkRecord, n=10101)
