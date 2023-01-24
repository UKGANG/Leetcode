"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def count_counterpart(colors, player):
            return sum(max(0, len(chunk) - 2) for chunk in colors.replace(player, ' ').split(' '))

        cnt_a = count_counterpart(colors, 'B')
        cnt_b = count_counterpart(colors, 'A')
        return cnt_a > cnt_b
