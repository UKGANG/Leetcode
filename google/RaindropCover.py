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