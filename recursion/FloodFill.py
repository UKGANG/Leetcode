'''
733. Flood Fill
https://leetcode.com/problems/flood-fill/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        cache = []
        for i in range(len(image)):
            cache.append([0] * len(image[0]))
        return self.recursiveFloodFill(image, sr, sc, image[sr][sc], newColor, cache)

    def recursiveFloodFill(self, image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int,
                           cache: List[List[int]]) -> List[List[int]]:
        cache[sr][sc] = 1
        image[sr][sc] = newColor
        if sr - 1 >= 0 and not cache[sr - 1][sc] and oldColor == image[sr - 1][sc]:
            self.recursiveFloodFill(image, sr - 1, sc, oldColor, newColor, cache)
        if sr + 1 < len(image) and not cache[sr + 1][sc] and oldColor == image[sr + 1][sc]:
            self.recursiveFloodFill(image, sr + 1, sc, oldColor, newColor, cache)
        if sc - 1 >= 0 and not cache[sr][sc - 1] and oldColor == image[sr][sc - 1]:
            self.recursiveFloodFill(image, sr, sc - 1, oldColor, newColor, cache)
        if sc + 1 < len(image[0]) and not cache[sr][sc + 1] and oldColor == image[sr][sc + 1]:
            self.recursiveFloodFill(image, sr, sc + 1, oldColor, newColor, cache)

        return image


assert_value([[2, 2, 2], [2, 2, 0], [2, 0, 1]], Solution().floodFill, image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1,
             sc=1, newColor=2)
assert_value([[2, 2, 2], [2, 2, 2]], Solution().floodFill, image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2)
