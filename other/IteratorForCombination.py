'''
1286. Iterator for Combination
https://leetcode.com/problems/iterator-for-combination/
'''
from typing import List

from test_tool import assert_value


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._len = len(characters)
        self._characters = characters
        self._combinationLength = combinationLength
        self._bitmask = (1 << self._len) - 1

    def next(self) -> str:
        while self._bitmask:
            try:
                if bin(self._bitmask).count('1') == self._combinationLength:
                    res = []
                    for i in range(self._len):
                        if self._bitmask & (1 << self._len - i - 1):
                            res.append(self._characters[i])
                    return ''.join(res)
            finally:
                self._bitmask -= 1

    def hasNext(self) -> bool:
        return self._bitmask >= (1 << self._combinationLength) - 1


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
param_1 = obj.next()
print(param_1)
param_2 = obj.hasNext()
print(param_2)
param_3 = obj.next()
print(param_3)
param_4 = obj.hasNext()
print(param_4)
param_5 = obj.next()
print(param_5)
param_6 = obj.hasNext()
print(param_6)
