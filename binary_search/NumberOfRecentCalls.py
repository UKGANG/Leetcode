'''
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
'''
import bisect


class RecentCounter:

    def __init__(self):
        self._pings = []

    def ping(self, t: int) -> int:
        self._pings.append(t)
        l, r = 0, len(self._pings)
        t -= 3000
        while l < r:
            m = l + ((r - l) >> 1)
            if self._pings[m] >= t:
                r = m
            else:
                l = m + 1

        return len(self._pings) - r

    def _ping(self, t: int) -> int:
        self._pings.append(t)
        return len(self._pings) - bisect.bisect_left(self._pings, t - 3000)