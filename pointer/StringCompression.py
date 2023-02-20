"""
443. String Compression
https://leetcode.com/problems/string-compression/
"""
from typing import List

from test_tool import assert_value


class Solution:
    def compress(self, chars: List[str]) -> int:
        idx_write, idx_group_name, idx_group_check = 0, 0, 1
        while idx_group_name < len(chars):
            while idx_group_check < len(chars) and chars[idx_group_check] == chars[idx_group_name]:
                idx_group_check += 1

            chars[idx_write] = chars[idx_group_name]
            idx_write += 1
            cnt = idx_group_check - idx_group_name
            if cnt > 1:
                cnt = str(cnt)
                for i in range(len(cnt)):
                    chars[idx_write] = cnt[i]
                    idx_write += 1
            idx_group_name = idx_group_check

        return idx_write

    def _compress(self, chars: List[str]) -> int:
        curr = 0
        left = 0
        right = 1
        while right < len(chars) + 1:
            if right == len(chars):
                chars[left] = chars[curr]
                left += 1
                if right - curr > 1:
                    cnt = str(right - curr)
                    for i in range(len(cnt)):
                        chars[left] = cnt[i]
                        left += 1
                break
            if chars[curr] != chars[right]:
                chars[left] = chars[curr]
                left += 1
                if right - curr > 1:
                    cnt = str(right - curr)
                    for i in range(len(cnt)):
                        chars[left] = cnt[i]
                        left += 1
                curr = right
            right += 1
        return left


assert_value(6, Solution().compress, chars=["a", "a", "b", "b", "c", "c", "c"])
assert_value(4, Solution().compress, chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
