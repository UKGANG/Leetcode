'''
2115. Find All Possible Recipes from Given Supplies
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ...


assert_value(1, Solution().findMinDifference, timePoints=["23:59", "00:00"])