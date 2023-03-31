"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l == r:
                return
            if l + 1 == r:
                nums[l], nums[r] = min(nums[l], nums[r]), max(nums[l], nums[r])
                return
            m = l + ((r - l) >> 1)
            mergeSort(l, m)
            mergeSort(m + 1, r)

            p = l
            p_l = l
            p_r = m + 1
            while p_l <= m and p_r <= r:
                if nums[p_l] < nums[p_r]:
                    cache[p] = nums[p_l]
                    p_l += 1
                else:
                    cache[p] = nums[p_r]
                    p_r += 1
                p += 1
            if p_l <= m:
                cache[p: r + 1] = nums[p_l: m + 1]
            if p_r <= r:
                cache[p: r + 1] = nums[p_r: r + 1]
            nums[l: r + 1] = cache[l: r + 1]

        n = len(nums)
        cache = [0] * n
        mergeSort(0, n - 1)
        return nums
