class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        total = 0
        stack = []
        for roman in s:
            if len(stack) == 0:
                if roman == "I" or roman == "X" or roman == "C":
                    stack.append(roman)
                else:
                    total += roman_dict[roman]
            else:
                word = stack[0] + roman
                if word not in roman_dict:
                    total += roman_dict[stack[0]]
                    stack[0] = roman
                else:
                    total += roman_dict[word]
                    stack = []
        if len(stack) > 0:
            total += roman_dict[stack[0]]
        return total
