'''
Find Valid Discount Coupons
https://algo.monster/problems/amazon_oa_valid_coupons
'''
from typing import List

from test_tool import assert_value


class Solution:
    def coupons(self, discounts: List[str]) -> List[int]:
        res = [0] * len(discounts)
        stack = []
        for idx, discount in enumerate(discounts):
            if len(discount) & 1:
                continue
            stack.clear()
            for c in discount:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
            if not stack:
                res[idx] = 1
        return res


assert_value([1, 0], Solution().coupons, discounts=['abba', 'abca'])
