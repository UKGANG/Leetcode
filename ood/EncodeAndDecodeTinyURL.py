'''
535. Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/
'''
import collections
import uuid
from typing import List

from test_tool import assert_value


class Codec:
    def __init__(self):
        self._cache = collections.defaultdict(lambda: '')

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = str(uuid.uuid4())
        self._cache[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self._cache[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))