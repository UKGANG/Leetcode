from typing import List


class Solution:
    def split(self, arr: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx == len(arr):
                nonlocal min_sum
                curr_res_sum = sorted(res_sum)
                curr_sum = curr_res_sum[-1] - curr_res_sum[0]
                if min_sum > curr_sum:
                    min_sum = curr_sum
                    for i, sub_arr in enumerate(curr):
                        res[i] = sub_arr[:]
                return
            if len(arr) - idx < sum(not bool(i) for i in res_sum):
                return

            for i in range(3):
                curr[i].append(arr[idx])
                res_sum[i] += arr[idx]
                backtrack(idx + 1)
                res_sum[i] -= arr[idx]
                curr[i].pop()

        res = [[], [], []]
        curr = [[], [], []]
        res_sum = [0, 0, 0]
        min_sum = float('inf')
        backtrack(0)
        return res


res = Solution().split([1, 2, 4, 5, 6])
print(res)
