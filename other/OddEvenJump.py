'''
975. Odd Even Jump
https://leetcode.com/problems/odd-even-jump/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        stack = []
        for num, idx in sorted([(n, idx) for idx, n in enumerate(arr)]):
            while stack and stack[-1] < idx:
                next_higher[stack.pop()] = idx
            stack.append(idx)

        stack.clear()
        for num, idx in sorted([(-n, idx) for idx, n in enumerate(arr)]):
            while stack and stack[-1] < idx:
                next_lower[stack.pop()] = idx
            stack.append(idx)

        stack.clear()

        high, low = [0] * n, [0] * n
        high[-1], low[-1] = 1, 1
        for idx in range(n - 2, -1, -1):
            high[idx] = low[next_higher[idx]]
            low[idx] = high[next_lower[idx]]

        return sum(high)


assert_value(2, Solution().oddEvenJumps, arr=[10, 13, 12, 14, 15])
assert_value(3, Solution().oddEvenJumps, arr=[2, 3, 1, 1, 4])
assert_value(3, Solution().oddEvenJumps, arr=[5, 1, 3, 4, 2])
