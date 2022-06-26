'''
Find Lowest Price
https://algo.monster/problems/amazon-oa-find-lowest-price
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findLowestPrice(self, products: List[List[str]], discounts: List[List[str]]) -> int:
        discount_type = [
            lambda val, price: price,
            lambda val, percentage: val * percentage,
            lambda val, off: val - off,
            lambda val, _: val,
        ]
        discount_map = {}
        for discount in discounts:
            discount_map[discount[0]] = (
                discount_type[int(discount[1] if discount[1].isnumeric() else -1)], float(discount[2])
            )
        res = 0
        for product in products:
            price = float(product[0])
            discounts = product[1:]
            min_price = price
            for discount_tag in discounts:
                if discount_tag not in discount_map:
                    continue
                discount_lambda, discount_factor = discount_map[discount_tag]
                min_price = min(min_price, discount_lambda(price, discount_factor))
            res += int(min_price)

        return res


assert_value(
    35,
    Solution().findLowestPrice,
    products=[['10', 'do', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY']],
    discounts=[['d0', '1', '27'], ['d1', '2', '5']]
)
