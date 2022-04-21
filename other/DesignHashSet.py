'''
705. Design HashSet
https://leetcode.com/problems/design-hashset/
'''


class MyHashSet:

    def __init__(self):
        self._cache = [False] * (10 ** 6)

    def add(self, key: int) -> None:
        self._cache[key - 1] = True

    def remove(self, key: int) -> None:
        self._cache[key - 1] = False

    def contains(self, key: int) -> bool:
        return self._cache[key - 1]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
