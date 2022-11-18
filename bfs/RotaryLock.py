import collections
from typing import (
    List,
)


class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """

    def open_lock(self, deadends: List[str], target: str) -> int:
        # Write your code here
        deadends = set(deadends)
        queue = collections.deque(['0000'])

        res = -1
        seen = set()
        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return res
                if curr in deadends:
                    continue
                if curr in seen:
                    continue
                seen.add(curr)
                for i in range(4):
                    num = int(curr[i])
                    num_prev = num + 10 - 1
                    num_prev %= 10
                    num_next = num + 1
                    num_next %= 10
                    queue.append(curr[:i] + str(num_prev) + curr[i + 1:])
                    queue.append(curr[:i] + str(num_next) + curr[i + 1:])

        return -1
