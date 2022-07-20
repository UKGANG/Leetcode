'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
'''
import bisect
from typing import List

from test_tool import assert_value


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        n_zeros = 0
        for n in nums:
            if n == 0:
                n_zeros += 1
                continue
            l, r = 0, len(res)
            n *= n
            while l < r:
                m = (l + r) >> 1
                if res[m] <= n:
                    l = m + 1
                else:
                    r = m
            res.insert(r, n)

        return [0] * n_zeros + res

    def _sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            bisect.insort_left(res, n ** 2)

        return res

    def _sortedSquares(self, nums: List[int]) -> List[int]:
        pos_list = []
        neg_list = []
        for num in nums:
            if num == 0:
                continue
            if num > 0:
                pos_list.append(num ** 2)
            else:
                neg_list.insert(0, num ** 2)

        res = []
        while neg_list or pos_list:
            if not len(neg_list):
                res += pos_list
                break
            if not len(pos_list):
                res += neg_list
                break
            if neg_list[0] > pos_list[0]:
                res.append(pos_list[0])
                del pos_list[0]
            else:
                res.append(neg_list[0])
                del neg_list[0]
        return [0] * (len(nums) - len(res)) + res


assert_value([0, 1, 9, 16, 100], Solution().sortedSquares, nums=[-4, -1, 0, 3, 10])
# assert_value([4, 9, 9, 49, 121], Solution().sortedSquares, nums=[-7, -3, 2, 3, 11])
# assert_value([0, 0, 25, 49, 99980001, 100000000, 100000000], Solution().sortedSquares,
#              nums=[-10000, -9999, -7, -5, 0, 0, 10000])
