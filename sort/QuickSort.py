'''
Quick Sort
https://wiki.jikexueyuan.com/project/easy-learn-algorithm/fast-sort.html
'''
from typing import List

from test_tool import assert_value


class Solution:
    def quickSort(self, target: List[int]) -> List[int]:
        if len(target) == 1:
            return target
        i = 1
        j = len(target) - 1

        while i < j:
            while target[j] > target[0] and j > 0:
                j -= 1
            while target[i] < target[0] and i < j:
                i += 1
            if i < j:
                target[i], target[j] = target[j], target[i]

        idx = min(i, j)
        if target[0] > target[idx]:
            target[0], target[idx] = target[idx], target[0]

        return self.quickSort(target[:i]) + self.quickSort(target[i:])


assert_value([1, 2, 3, 4, 5, 123], Solution().quickSort, target=[1, 2, 3, 4, 5, 123])
assert_value([5, 123], Solution().quickSort, target=[5, 123])
assert_value([0, 1, 2, 3, 10, 50], Solution().quickSort, target=[3, 10, 50, 2, 1, 0])
