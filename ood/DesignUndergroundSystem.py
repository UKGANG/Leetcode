'''
1396. Design Underground System
https://leetcode.com/problems/design-underground-system/
'''
import collections
from collections import defaultdict
from test_tool import assert_value


class UndergroundSystem:

    def __init__(self):
        self._online_log = {}
        self._offline_log = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._online_log[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationName_start, t_start = self._online_log[id]
        del self._online_log[id]
        self._offline_log[(stationName_start, stationName)].append(t - t_start)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_logs = self._offline_log[(startStation, endStation)]
        return sum(time_logs) / len(time_logs)


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
assert_value(14, undergroundSystem.getAverageTime, startStation='Paradise', endStation='Cambridge')
assert_value(11, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Waterloo')
undergroundSystem.checkIn(10, "Leyton", 24)
assert_value(11, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Waterloo')
undergroundSystem.checkOut(10, "Waterloo", 38)
assert_value(12, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Waterloo')

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
assert_value(5, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Paradise')
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
assert_value(5.5, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Paradise')
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
assert_value(40 / 6, undergroundSystem.getAverageTime, startStation='Leyton', endStation='Paradise')
undergroundSystem.getAverageTime("Leyton", "Paradise")
