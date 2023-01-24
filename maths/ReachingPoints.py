"""
780. Reaching Points
https://leetcode.com/problems/reaching-points/description/
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        if sx == tx and sy <= ty and (ty - sy) % sx == 0:
            return True

        return sy == ty and sx <= tx and (tx - sx) % sy == 0
