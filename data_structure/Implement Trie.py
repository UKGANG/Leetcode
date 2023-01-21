"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
from typing import Dict


class TrieNode:
    def __init__(self):
        self._is_word: bool = None
        self._children: Dict[str, TrieNode] = {}

    @property
    def is_word(self) -> bool:
        return self._is_word

    @is_word.setter
    def is_word(self, is_word: str):
        self._is_word = is_word

    @property
    def children(self) -> Dict[str, 'TrieNode']:
        return self._children

    @children.setter
    def children(self, children: str):
        self._children = children


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.search("app")
param_4 = obj.startsWith("app")
obj.insert("app")
param_5 = obj.search("app")
