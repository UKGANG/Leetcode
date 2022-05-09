'''
815. Bus Routes
https://leetcode.com/problems/bus-routes/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        station_map = collections.defaultdict(set)
        for route_id, stops in enumerate(routes):
            for stop in stops:
                station_map[stop].add(route_id)

        graph = collections.defaultdict(set)
        for station in station_map.values():
            for route_id in station:
                graph[route_id].update(station)

        curr_level = set(station_map[source])
        routes = [set(stops) for stops in routes]

        visited = set()
        res = 0
        while curr_level:
            next_level = set()
            res += 1
            for route_id in curr_level:
                if target in routes[route_id]:
                    return res
                visited.add(route_id)
                for next_route_id in graph[route_id]:
                    if next_route_id in visited:
                        continue
                    next_level.add(next_route_id)

            curr_level = next_level
        return -1


assert_value(2, Solution().numBusesToDestination,
             routes=[[1, 2, 7], [3, 6, 7]],
             source=1,
             target=6)
assert_value(-1, Solution().numBusesToDestination,
             routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]],
             source=15,
             target=12)
assert_value(0, Solution().numBusesToDestination,
             routes=[[1,7],[3,5]],
             source=5,
             target=5)
