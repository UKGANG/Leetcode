'''
1396. Design Underground System
https://leetcode.com/problems/design-underground-system/
'''
from collections import defaultdict
from test_tool import assert_value


class UndergroundSystem:

    def __init__(self):
        self._id_cache = {}
        self._station_cache = defaultdict(set)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        transaction = Transaction(id, stationName, t)
        self._id_cache[id] = transaction
        self._station_cache[stationName].add(transaction)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self._id_cache[id].checkOut(stationName, t)
        self._station_cache[stationName].add(self._id_cache[id])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        txns = self._station_cache[startStation]
        txns = [txn for txn in txns if txn in self._station_cache[endStation]]
        txns = [txn for txn in txns if txn.end]
        total = [txn.end - txn.begin for txn in txns]
        return sum(total) / len(total)


class Transaction:
    def __init__(self, id: int, checkin_station: str, begin: int):
        self._id = id
        self._checkin_station = checkin_station
        self._begin = begin

    def checkOut(self, checkout_station: str, end: int):
        self._checkout_station = checkout_station
        self._end = end

    @property
    def begin(self):
        return self._begin

    @property
    def end(self):
        return self._end


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
