from typing import List
from typing import Tuple

from test_tool import assert_value


class Solution:
    def intervia_divide(
            self, a: List[Tuple[float, float, int]], b: List[Tuple[float, float, int]]
    ) -> List[Tuple[float, float, int]]:
        if a[0][0] != 0:
            if a[0][-1] == 0:
                a[0][0] = 0
            else:
                a.insert(0, (0, a[0][0], 0))
        if a[-1][1] != 1:
            if a[-1][-1] == 0:
                a[-1][1] = 1
            else:
                a.append((a[-1][1], 1, 0))
        start = 0
        idx_a = idx_b = 0
        res = []
        while idx_a < len(a) and idx_b < len(b):
            tuple_a = a[idx_a]
            tuple_b = b[idx_b]
            if tuple_a[1] > tuple_b[1]:
                end = tuple_b[1]
                res.append(
                    (start, end,
                     (tuple_a[-1] / tuple_b[-1]) if tuple_b[-1] else 0
                     )
                )
                idx_b += 1
            else:
                end = tuple_a[1]
                res.append(
                    (start, end,
                     (tuple_a[-1] / tuple_b[-1]) if tuple_b[-1] else 0
                     )
                )
                idx_a += 1
            start = end
        return res


assert_value(
    [(0, 0.2, 0), (0.2, 0.3, 1), (0.3, 0.5, 0.5), (0.5, 1, 0)],
    Solution().intervia_divide, a=[(0.2, 0.5, 1)], b=[(0, 0.3, 1), (0.3, 1, 2)]
)
