'''
2115. Find All Possible Recipes from Given Supplies
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        missing_cnt = collections.Counter()
        missing_ingredient_recipe = collections.defaultdict(set)
        res = []
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                if item not in supplies:
                    missing_cnt[recipe] += 1
                    missing_ingredient_recipe[item].add(recipe)
            if not missing_cnt[recipe]:
                res.append(recipe)

        for ingredient in res:
            for recipe in missing_ingredient_recipe[ingredient]:
                missing_cnt[recipe] -= 1
                if not missing_cnt[recipe]:
                    res.append(recipe)
        return res

    def _findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        supplies = set(supplies)
        for _ in range(len(recipes)):
            for idx, recipe in enumerate(recipes):
                if recipe in supplies:
                    continue
                for ingredient in ingredients[idx]:
                    if ingredient not in supplies:
                        break
                else:
                    res.append(recipe)
                    supplies.add(recipe)
        return res


assert_value(["bread"], Solution().findAllRecipes,
             recipes=["bread"],
             ingredients=[["yeast", "flour"]],
             supplies=["yeast", "flour", "corn"])
assert_value(["bread", "sandwich"], Solution().findAllRecipes,
             recipes=["bread", "sandwich"],
             ingredients=[["yeast", "flour"], ["bread", "meat"]],
             supplies=["yeast", "flour", "meat"])
assert_value(["bread", "sandwich", "burger"], Solution().findAllRecipes,
             recipes=["bread", "sandwich", "burger"],
             ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
             supplies=["yeast", "flour", "meat"])
