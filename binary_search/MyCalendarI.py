'''
729. My Calendar I
https://leetcode.com/problems/my-calendar-i/
'''
from bisect import bisect
from operator import itemgetter


class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        idx_start = bisect.bisect_right(self.bookings, start)
        idx_end = bisect.bisect_left(self.bookings, end)

        if idx_start & 1 or idx_start != idx_end:
            return False

        self.bookings[idx_start:idx_start] = [start, end]

        return True

    def _book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append((start, end))
            return True
        idx = bisect.bisect_left(self.bookings, start, key=itemgetter(0))
        if 0 == idx:
            if self.bookings[0][0] < end:
                return False
            self.bookings.insert(idx, (start, end))
            return True
        if len(self.bookings) == idx:
            if self.bookings[-1][1] > start:
                return False
            self.bookings.append((start, end))
            return True
        if self.bookings[idx][0] < end or self.bookings[idx - 1][1] > start:
            return False
        self.bookings.insert(idx, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
