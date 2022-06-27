'''
Transaction logs
https://leetcode.com/discuss/interview-question/989768/amazon-oa-2020-transaction-logs
'''
from typing import List

from test_tool import assert_value


class Solution:
    def processLogs(self, logs: List[str], threshold: int) -> List[str]:
        cache = {}
        for log in logs:
            sender_id, receiver_id, amt = log.split(' ')
            if sender_id != receiver_id:
                cache[sender_id] = cache.get(sender_id, 0) + 1
            cache[receiver_id] = cache.get(receiver_id, 0) + 1
        user_ids = [int(k) for k, v in cache.items() if v >= threshold]
        user_ids = sorted(user_ids)
        return [str(user_id) for user_id in user_ids]
