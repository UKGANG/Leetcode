"""
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        one = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        teen = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        ten = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def convertHundred(num):
            hundred, tens = divmod(num, 100)
            if hundred:
                words.append(one[hundred])
                words.append("Hundred")

            # tens, num = divmod(tens, 10)
            if 10 <= tens <= 19:
                words.append(teen[tens])
            else:
                if tens >= 20:
                    words.append(ten[int(tens / 10) * 10])
                tens, num = divmod(tens, 10)
                if num:
                    words.append(one[num])

        billion = int(num / (1000 ** 3))
        million = int(num % (1000 ** 3) / (1000 ** 2))
        thousand = int(num % (1000 ** 2) / 1000)
        hundred = num % 1000

        words = []
        if billion:
            convertHundred(billion)
            words.append("Billion")
        if million:
            convertHundred(million)
            words.append("Million")
        if thousand:
            convertHundred(thousand)
            words.append("Thousand")
        if hundred:
            convertHundred(hundred)

        return " ".join(words)
