import bisect
from operator import itemgetter
from typing import List


class RaindropCover:

    def cover(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 0 or arr[-1] < 99:
            return False

        res = 1
        interval_prev = interval_curr = arr[0]
        for i in range(1, len(arr)):
            interval_next = arr[i]
            if interval_next - 1 > interval_prev:
                if interval_next - 1 > interval_curr:
                    return False
                interval_prev, interval_curr = interval_curr, interval_next
                res += 1
            else:
                interval_curr = interval_next

        return res

    def check_cover(self, arr: List[int]) -> int:
        class SearchableList:
            def __init__(self, arr, key):
                self.arr = arr
                self.key = key

            def __len__(self):
                return len(self.arr)

            def __getitem__(self, item):
                return self.key(self.arr[item])

        interval = [[arr[0], arr[0] + 1]]
        res = 1
        for pos in arr[1:]:
            new_interval = [pos, pos + 1]
            idx_left = bisect.bisect(SearchableList(interval, key=itemgetter(0)), new_interval[0])
            idx_right = bisect.bisect(SearchableList(interval, key=itemgetter(0)), new_interval[1])

            if interval[max(idx_left - 1, 0)][1] > new_interval[0]:
                idx_left = max(idx_left - 1, 0)
                new_interval[0] = interval[idx_left][0]
            idx_right = min(len(interval) - 1, idx_right)

            if new_interval[0] < interval[idx_left][0] or interval[idx_right][1] < new_interval[1]:
                res += 1
                del interval[idx_left: idx_right + 1]
                interval.insert(idx_left, new_interval)

        return -1 if len(interval) != 1 or (interval[0][0] != 0 and interval[0][1] < 5) else res


res = RaindropCover().check_cover([i / 2 for i in range(10)] * 2)
print(res)
