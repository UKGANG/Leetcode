from typing import List
from typing import Tuple

from test_tool import assert_value


class Solution:
    def guest_count(self, N: int, tickets: List[Tuple[int, int]]) -> List[int]:
        delta = [0] * N
        for start, end in tickets:
            delta[start] += 1
            if end + 1 < N:
                delta[end + 1] -= 1
        for i in range(1, N):
            delta[i] += delta[i - 1]
        return delta


assert_value(
    [0, 1, 2, 2, 1],
    Solution().guest_count, N=5, tickets=[(1, 3), (2, 4)]
)
