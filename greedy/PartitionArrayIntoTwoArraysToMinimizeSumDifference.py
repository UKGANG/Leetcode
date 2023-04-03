"""
2035. Partition Array Into Two Arrays to Minimize Sum Difference
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference
"""
import bisect
import collections
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        left_combo = collections.defaultdict(list)
        right_combo = collections.defaultdict(list)

        left_combo[0].append(0)
        right_combo[0].append(0)

        for i in range(n >> 1):
            for j in range(i, -1, -1):
                base_combo = left_combo[j]
                new_combo = left_combo[j + 1]

                for sub_total in base_combo:
                    new_combo.append(sub_total + nums[i])

        for i in range(n >> 1, n):
            for j in range(i, -1, -1):
                base_combo = right_combo[j]
                new_combo = right_combo[j + 1]

                for sub_total in base_combo:
                    new_combo.append(sub_total + nums[i])

        for cnt in left_combo.keys():
            left_combo[cnt] = sorted(list(set(left_combo[cnt])))

        for cnt in right_combo.keys():
            right_combo[cnt] = list(set(right_combo[cnt]))

        res = float('inf')
        for i in range(n >> 1):
            right_cnt = i
            right_combo_sub = right_combo[right_cnt]

            left_cnt = (n >> 1) - i
            left_combo_sub = left_combo[left_cnt]

            for right_sum in right_combo_sub:
                remaining = (total >> 1) - right_sum
                idx = bisect.bisect(left_combo_sub, remaining)

                idx = idx if idx < len(left_combo_sub) else idx - 1
                left_sum = left_combo_sub[idx]
                res = min(res, abs(total - ((left_sum + right_sum) << 1)))
                if not res:
                    return res

                idx = idx if idx == 0 else idx - 1
                left_sum = left_combo_sub[idx]
                res = min(res, abs(total - ((left_sum + right_sum) << 1)))

        return res
