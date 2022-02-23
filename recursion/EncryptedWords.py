'''
Encrypted Words
https://codepen.io/rupeshtiwari/pen/VwpoEgb
'''
from test_tool import assert_value


def findEncryptedWord(s):
    # Write your code here
    if not s:
        return ''
    idx_mid = (len(s) - 1) >> 1
    res = [s[idx_mid], findEncryptedWord(s[:idx_mid]), findEncryptedWord(s[idx_mid + 1:])]
    return ''.join(res)


assert_value("bac", findEncryptedWord, s="abc")
assert_value("bacd", findEncryptedWord, s="abcd")
assert_value("xbacbca", findEncryptedWord, s="abcxcba")
assert_value("eafcobok", findEncryptedWord, s="facebook")
