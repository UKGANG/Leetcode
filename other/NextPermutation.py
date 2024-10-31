'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/
'''
from typing import List

import numpy

from test_tool import assert_value


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                continue
            pivot = i
            left = i - 1

            right = pivot
            for j in range(pivot, len(nums)):
                if nums[left] < nums[j]:
                    right = j
                else:
                    break
            nums[left], nums[right] = nums[right], nums[left]
            nums[pivot:] = nums[pivot::-1]
            break
        else:
            nums.reverse()

    def _nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                continue
            head = i - 1
            tail = i
            for j in range(tail, len(nums)):
                if nums[j] > nums[head]:
                    tail = j
                else:
                    break
            nums[head], nums[tail] = nums[tail], nums[head]

            head = i
            for j in range((len(nums) - i) >> 1):
                nums[head + j], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[head + j]
            break
        else:
            nums.reverse()

    def __nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                continue
            head = i - 1
            min_j = nums[head]
            tail = head + 1
            for i in range(head + 1, len(nums)):
                if nums[i] > min_j:
                    tail = i
            nums[head], nums[tail] = nums[tail], nums[head]

            for i in range((len(nums) - head - 1) >> 1):
                nums[head + 1 + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[head + 1 + i]
            break
        else:
            nums.reverse()


assert_value([1, 3, 2], Solution().nextPermutation, nums=[1, 2, 3])
assert_value([1, 2, 3], Solution().nextPermutation, nums=[3, 2, 1])
assert_value([1, 5, 1], Solution().nextPermutation, nums=[1, 1, 5])
assert_value([2, 1, 3], Solution().nextPermutation, nums=[1, 3, 2])
assert_value([2, 3, 3, 1, 3], Solution().nextPermutation, nums=[2, 3, 1, 3, 3])
