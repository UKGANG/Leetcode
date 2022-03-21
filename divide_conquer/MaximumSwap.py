'''
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/
'''
import heapq

from test_tool import assert_value


class Solution:
    def maximumSwap(self, num: int) -> int:
        max_cache = []
        num = list(str(num))
        for idx, n in enumerate(num):
            heapq.heappush(max_cache, (-int(n), -idx))
        idx_right = 0
        idx_left = idx_right
        while max_cache:
            _, idx = heapq.heappop(max_cache)
            idx = -idx
            for i in range(idx):
                if num[i] < num[idx]:
                    idx_left = i
                    idx_right = idx
                    break
            if idx_left != idx_right:
                break

        num[idx_left], num[idx_right] = num[idx_right], num[idx_left]
        return int(''.join(num))

    def maximumSwap_v1(self, num: int) -> int:
        num_str = str(num)
        # base case
        if len(num_str) == 1:
            return num_str
        elif len(num_str) == 2:
            return max(num_str, num_str[::-1])

        mid = int(len(num_str) / 2)
        left = self.maximumSwap(num_str[:mid])
        right = self.maximumSwap(num_str[mid:])
        left = str(left) + num_str[mid:]
        right = num_str[:mid] + str(right)

        left_swap = 0
        for i in reversed(range(10)[1:]):
            for j in reversed(range(mid, len(num_str))):
                if i == int(num_str[j]):
                    left_swap = j
                    break
            else:
                continue
            break

        right_swap = 0
        while num_str[right_swap] >= num_str[left_swap] and right_swap < left_swap:
            right_swap += 1
        if left_swap == right_swap:
            return int(max(left, right))
        edge = [c for c in num_str]
        edge[left_swap], edge[right_swap] = edge[right_swap], edge[left_swap]
        edge = ''.join(edge)
        return int(max(max(left, right), edge))


assert_value(7236, Solution().maximumSwap, num=2736)
assert_value(9973, Solution().maximumSwap, num=9973)
assert_value(98863, Solution().maximumSwap, num=98368)
assert_value(91000000, Solution().maximumSwap, num=90000001)
assert_value(9913, Solution().maximumSwap, num=1993)
assert_value(1, Solution().maximumSwap, num=1)
assert_value(10, Solution().maximumSwap, num=10)
assert_value(52341342, Solution().maximumSwap, num=22341345)
