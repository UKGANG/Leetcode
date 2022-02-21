'''
Largest Triple Products
https://www.geeksforgeeks.org/largest-triplet-product-stream/
'''
import bisect
from typing import List

from test_tool import assert_value


def findMaxProduct(arr):
    top_3 = []
    res = []
    for i in arr:
        bisect.insort(top_3, i)

        prod = 1
        if len(top_3) > 2:
            if len(top_3) > 3:
                top_3 = top_3[1:]
            for j in top_3:
                prod *= j
        else:
            prod = -1

        res.append(prod)
    return res


assert_value([-1, -1, 6, 24, 60], findMaxProduct, arr=[1, 2, 3, 4, 5])
assert_value([-1, -1, 4, 4, 8], findMaxProduct, arr=[2, 1, 2, 1, 2])
