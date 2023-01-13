'''
468. Validate IP Address
https://leetcode.com/problems/validate-ip-address/
'''


class Solution:
    def validIPV4(self, queryIP: str) -> str:
        chunks = queryIP.split(".")
        if len(chunks) != 4:
            return 'Neither'
        for chunk in chunks:
            if chunk.startswith("0") and len(chunk) > 1:
                return 'Neither'
            try:
                num = int(chunk)
                if not 0 <= num <= 255:
                    return 'Neither'
            except:
                return 'Neither'
        return 'IPv4'

    def validIPV6(self, queryIP: str) -> str:
        chunks = queryIP.split(":")
        if len(chunks) != 8:
            return 'Neither'
        for chunk in chunks:
            if not 1 <= len(chunk) <= 4:
                return 'Neither'
            for c in chunk:
                if not c.isdigit() and c not in "abcdefABCDEF":
                    return 'Neither'
        return 'IPv6'

    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            return self.validIPV4(queryIP)
        elif ':' in queryIP:
            return self.validIPV6(queryIP)
        else:
            return 'Neither'
