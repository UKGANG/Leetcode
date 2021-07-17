'''
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sub_sum, resid = divmod(sum(nums), k)
        if resid:
            return False
        nums = sorted(nums, reverse=True)

        bucket = [sub_sum] * k
        return self.greedy_fill(sub_sum, nums, bucket, 0)

    def greedy_fill(self, sub_sum, nums, bucket, idx_curr):
        if idx_curr == len(nums):
            return not sum(bucket)
        for slot in range(len(bucket)):
            if not bucket[slot]:
                continue
            bucket[slot] -= nums[idx_curr]
            if bucket[slot] >= 0 and self.greedy_fill(sub_sum, nums, bucket, idx_curr + 1):
                return True
            bucket[slot] += nums[idx_curr]
            if bucket[slot] == sub_sum:
                break
        return False


assert_value(True, Solution().canPartitionKSubsets, nums=[4, 3, 2, 3, 5, 2, 1], k=4)
assert_value(False, Solution().canPartitionKSubsets, nums=[1, 2, 3, 4], k=3)
