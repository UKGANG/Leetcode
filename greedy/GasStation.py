'''
134. Gas Station
https://leetcode.com/problems/gas-station/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        available_min = float('inf')
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            total += rest
            available_min = min(available_min, total)

        if total < 0:
            return -1
        if available_min >= 0:
            return 0
        for i in range(len(gas) - 1, -1, -1):
            available_min += gas[i] - cost[i]
            if available_min >= 0:
                return i
        return -1

    def _canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        available = 0
        start = 0
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            total += rest
            available += rest
            if available < 0:
                start = i + 1
                available = 0

        if total < 0:
            return -1
        return start

    def __canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        travel_range_curr = 0
        travel_range_cost = 0
        res = 0
        for i in range(len(gas) * 2):
            travel_range_curr += gas[i % len(gas)]
            travel_range_cost += cost[i % len(gas)]
            if travel_range_curr < travel_range_cost:
                travel_range_curr = 0
                travel_range_cost = 0
                res = 0
            else:
                res += 1
                if res == len(gas):
                    return i - res + 1

        return -1
