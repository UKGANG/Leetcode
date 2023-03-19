"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/
"""
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks).values()
        frequencies = list(frequencies)
        frequencies.sort()

        res = 0
        while len(frequencies) >= n + 1:
            for i in range(n + 1):
                frequencies[~i] -= 1
            res += n + 1
            frequencies = [cnt for cnt in frequencies if cnt]
            frequencies.sort()

        if not frequencies:
            return res

        n_max = frequencies.count(frequencies[-1])
        res += (n + 1) * (frequencies[-1] - 1) + n_max
        return res
