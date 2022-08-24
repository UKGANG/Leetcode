'''
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/
'''
import functools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, section_cnt):
            if not section_cnt:
                if start == len(s):
                    res.append(combo[:])
                return
            if start == len(s):
                return

            for end in range(start + 1, len(s) + 1):
                if end > start + 4:
                    break
                if len(s) - end + 1 < section_cnt:
                    break
                if s[start] == '0' and end - start > 1:
                    break
                ip = s[start: end]
                if int(ip) > 255:
                    break
                combo.append(ip)
                backtrack(end, section_cnt - 1)
                combo.pop()

        if len(s) < 4 or len(s) > 12:
            return []
        res, combo = [], []
        backtrack(0, 4)
        return ['.'.join(ip) for ip in res]
