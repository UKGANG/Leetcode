import collections
from typing import List

from test_tool import assert_value


class Point:
    x: int
    y: int


class LineSegment:
    start: Point
    end: Point


class Solution:
    def countSquare(self, lines: List[LineSegment]) -> int:
        cache = collections.defaultdict(set)

        for line in lines:
            cache[(line.start.x, line.start.y)].add(line)
            cache[(line.end.x, line.end.y)].add(line)

        point_cache_list = list(cache.items())

        res = 0
        for i in range(len(point_cache_list) - 1):
            for j in range(i + 1, len(point_cache_list)):
                (x1, y1), lines_1 = point_cache_list[i]
                (x2, y2), lines_3 = point_cache_list[j]
                if x1 == x2 or y1 == y2:
                    continue

                lines_2 = cache[(x1, y2)]
                lines_4 = cache[(x2, y1)]

                line1_cnt = len(lines_1.intersection(lines_2))
                line2_cnt = len(lines_2.intersection(lines_3))
                line3_cnt = len(lines_3.intersection(lines_4))
                line4_cnt = len(lines_4.intersection(lines_1))

                res += (line1_cnt * line2_cnt * line3_cnt * line4_cnt)

        return res >> 1

p1: Point = Point()
p1.x = 1
p1.y = 1

p2: Point = Point()
p2.x = 1
p2.y = 2

p3: Point = Point()
p3.x = 2
p3.y = 2

p4: Point = Point()
p4.x = 2
p4.y = 1

line1 = LineSegment()
line1.start = p1
line1.end = p2

line2 = LineSegment()
line2.start = p2
line2.end = p3

line3 = LineSegment()
line3.start = p3
line3.end = p4

line4 = LineSegment()
line4.start = p4
line4.end = p1

lines = [line1, line2, line3,line4]
assert_value(1, Solution().countSquare, lines=lines)
