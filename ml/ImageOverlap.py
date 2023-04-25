"""
835. Image Overlap
https://leetcode.com/problems/image-overlap
"""
import itertools
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def padding(img):
            nonlocal n
            padding_img = [
                [0] * (n * 3 - 2) for _ in range(n * 3 - 2)
            ]
            for x, y in itertools.product(range(n), range(n)):
                padding_img[x + n - 1][y + n - 1] = img[x][y]
            return padding_img

        def convolute(kernel, img, x, y):
            res = 0
            for i, j in itertools.product(range(n), range(n)):
                res += kernel[i][j] * img[i + x][j + y]
            return res

        n = len(img1)
        padding_img = padding(img2)

        res = 0
        for x, y in itertools.product(range((n << 1) - 1), range((n << 1) - 1)):
            res = max(res, convolute(img1, padding_img, x, y))
        return res
