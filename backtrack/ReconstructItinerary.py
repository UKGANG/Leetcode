'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(depature):
            if len(combo) - 1 == len(tickets):
                return True

            arrival_list = graph[depature]
            size = len(arrival_list)
            for _ in range(size):
                arrival = arrival_list.pop(0)
                combo.append(arrival)
                if backtrack(arrival):
                    return True
                combo.pop()
                arrival_list.append(arrival)

        graph = collections.defaultdict(list)
        for depature, arrival in tickets:
            graph[depature].append(arrival)

        for depature in graph.keys():
            graph[depature] = sorted(graph[depature])
        combo = ['JFK']
        backtrack('JFK')
        return combo
