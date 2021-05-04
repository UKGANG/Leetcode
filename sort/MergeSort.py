'''
Merge Sort
https://zhuanlan.zhihu.com/p/124356219
'''
from typing import List
from test_tool import assert_value


class Solution:
    def mergeSort(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums

        left = self.mergeSort(nums[:len(nums) // 2])
        right = self.mergeSort(nums[len(nums) // 2:])

        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                min_num = left[i]
                i += 1
            else:
                min_num = right[j]
                j += 1
            result.append(min_num)

        if i < len(left):
            result = result + left[i:]

        if j < len(right):
            result = result + right[j:]

        return result


assert_value([1, 2, 3, 4, 5, 123], Solution().mergeSort, nums=[3, 2, 4, 1, 123, 5])
