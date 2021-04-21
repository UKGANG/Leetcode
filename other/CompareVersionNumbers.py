'''
165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        slot1 = version1.split('.')
        slot2 = version2.split('.')
        for i in range(max(len(slot1), len(slot2))):
            v1 = 0 if i >= len(slot1) else int(slot1[i])
            v2 = 0 if i >= len(slot2) else int(slot2[i])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


assert_value(0, Solution().compareVersion, version1="1.01", version2="1.001")
assert_value(0, Solution().compareVersion, version1="1.0", version2="1.0.0")
assert_value(-1, Solution().compareVersion, version1="0.1", version2="1.1")
assert_value(1, Solution().compareVersion, version1="1.0.1", version2="1")
assert_value(-1, Solution().compareVersion, version1="7.5.2.4", version2="7.5.3")
