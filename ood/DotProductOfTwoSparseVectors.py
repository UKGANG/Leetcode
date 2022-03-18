'''
1570. Dot Product of Two Sparse Vectors
https://leetcode.ca/all/1570.html
'''
from typing import List

from test_tool import assert_value


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {idx: num for idx, num in enumerate(nums) if num}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        keys = set()
        keys_1 = self.nums.keys()
        keys_2 = vec.nums.keys()
        res = 0
        for key in keys_1:
            keys.add(key)
        for key in keys_2:
            keys.add(key)
        for key in keys:
            if key not in keys_1 or key not in keys_2:
                continue
            res += (self.nums[key] * vec.nums[key])
        return res


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert_value(8, v1.dotProduct, vec=v2)

nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert_value(0, v1.dotProduct, vec=v2)

nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
assert_value(6, v1.dotProduct, vec=v2)
