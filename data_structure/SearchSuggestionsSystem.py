'''
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
'''
import bisect
import collections
from typing import List

from test_tool import assert_value


class Node:
    def __init__(self, c: str, prefix_cache):
        self._c = c
        self._is_word = False
        self._suffix_cache = collections.OrderedDict()
        self._prefix_cache = prefix_cache

    @property
    def char(self):
        return self._c

    @property
    def suffix_cache(self):
        return self._suffix_cache

    @property
    def prefix_cache(self):
        return self._prefix_cache

    @property
    def is_word(self):
        return self._is_word

    @is_word.setter
    def is_word(self, is_word):
        self._is_word = is_word


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tier = Node(None, None)
        for product in products:
            cache = tier
            for c in product:
                if c not in cache.suffix_cache:
                    cache.suffix_cache[c] = Node(c, cache)
                cache = cache.suffix_cache[c]

            cache.is_word = True

        res = []
        for idx in range(len(searchWord)):
            res.append(self.search_by_key(tier, searchWord[:idx + 1]))

        return res

    def search_by_key(self, cache: Node, keyword: str) -> List[str]:
        for c in keyword:
            if c not in cache.suffix_cache:
                return []
            cache = cache.suffix_cache[c]

        res = []
        stack = [cache]
        while stack and len(res) < 3:
            cache = stack.pop()
            if cache.is_word:
                res.append(self.extract_prefix(cache))
            for c, node in sorted(cache.suffix_cache.items(), reverse=True):
                stack.append(node)

        return sorted(res)

    def extract_prefix(self, cache: Node):
        word = []
        while cache.char:
            word.insert(0, cache.char)
            cache = cache.prefix_cache

        return ''.join(word)

    def _suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        idx, out, prefix = 0, [], ""
        for c in searchWord:
            prefix += c
            idx = bisect.bisect_left(products, prefix)
            temp = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i][:len(prefix)] != prefix:
                    break
                temp.append(products[i])
            out.append(temp)
        return out


assert_value([
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"]
], Solution().suggestedProducts, products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse")

assert_value([["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]], Solution().suggestedProducts,
             products=["havana"], searchWord="havana")

assert_value([["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]],
             Solution().suggestedProducts, products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags")

assert_value([[], [], [], [], [], [], []], Solution().suggestedProducts, products=["havana"], searchWord="tatiana")
