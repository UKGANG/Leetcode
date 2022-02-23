'''
Change in a Foreign Currency
https://leetcode.com/discuss/interview-question/999637/facebook-online-change-in-a-foreign-currency
'''
from test_tool import assert_value


def canGetExactChange(targetMoney, denominations):
    dp = [0] * (targetMoney + 1)
    denominations = sorted(denominations)
    denominations = [cash for cash in denominations if cash <= targetMoney]
    for cash in denominations:
        dp[cash] = True
    for i in range(1, targetMoney + 1):
        for cash in denominations:
            if i - cash > 0 and dp[i - cash]:
                dp[i] = True
    return dp[-1]


assert_value(False, canGetExactChange, targetMoney=94, denominations=[5, 10, 25, 100, 200])
assert_value(True, canGetExactChange, targetMoney=75, denominations=[4, 17, 29])
