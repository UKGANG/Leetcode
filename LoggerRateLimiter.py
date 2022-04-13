'''
359. Logger Rate Limiter
https://leetcode.com/problems/logger-rate-limiter/
'''
from typing import List, Optional

from test_tool import assert_value


class Logger:

    def __init__(self):
        self._cache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._cache:
            self._cache[message] = timestamp
            return True
        if timestamp - self._cache[message] >= 10:
            self._cache[message] = timestamp
            return True
        return False
