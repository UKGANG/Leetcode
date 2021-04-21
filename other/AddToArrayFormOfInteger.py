'''
989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n1 = ''.join(str(n) for n in A)
        return [int(c) for c in str(K + int(n1))]


assert_value([1, 2, 3, 4], Solution().addToArrayForm, A=[1, 2, 0, 0], K=34)
assert_value([4, 5, 5], Solution().addToArrayForm, A=[2, 7, 4], K=181)
assert_value([1, 0, 2, 1], Solution().addToArrayForm, A=[2, 1, 5], K=806)
assert_value([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], Solution().addToArrayForm, A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1)
