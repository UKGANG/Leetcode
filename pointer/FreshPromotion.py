'''
Amazon | OA 2021 | Fresh Promotion
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._anything = 'anything'

    def isFreshPromotion(self, codeList: List[List[str]], shoppingCart: List[str]) -> int:
        shoppingCart
        start_idx_cart = 0
        for codeGroup in codeList:
            if len(shoppingCart) == start_idx_cart:
                return 0
            start_idx_cart = self.matchGroup(codeGroup, shoppingCart, start_idx_cart)
            if -1 == start_idx_cart:
                return 0
        return 1

    def matchGroup(self, codeGroup: List[str], shoppingCart: List[str], start_idx_cart) -> int:
        group_idx = 0
        cart_idx = start_idx_cart
        while group_idx < len(codeGroup) and cart_idx < len(shoppingCart):
            if codeGroup[group_idx] in [self._anything, shoppingCart[cart_idx]]:
                group_idx += 1
            else:
                group_idx = 0
            cart_idx += 1

        return cart_idx if group_idx == len(codeGroup) else -1


assert_value(1, Solution().isFreshPromotion, codeList=[['apple', 'apple'], ['banana', 'anything', 'banana']],
             shoppingCart=['orange', 'apple', 'apple', 'banana', 'orange', 'banana'])
assert_value(0, Solution().isFreshPromotion, codeList=[['apple', 'apple'], ['banana', 'anything', 'banana']],
             shoppingCart=['banana', 'orange', 'banana', 'apple', 'apple'])
assert_value(0, Solution().isFreshPromotion, codeList=[['apple', 'apple'], ['banana', 'anything', 'banana']],
             shoppingCart=['apple', 'banana', 'apple', 'banana', 'orange', 'banana'])
assert_value(0, Solution().isFreshPromotion, codeList=[['apple', 'apple'], ['apple', 'apple', 'banana']],
             shoppingCart=['apple', 'apple', 'apple', 'banana'])
