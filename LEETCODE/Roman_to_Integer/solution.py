class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        total = 0
        while i < len(s):
            numeral = s[i]

            if numeral in ['I', 'X', 'C'] and i + 1 < len(s):
                n = s[i+1]
                if numeral == 'I' and n in ['V', 'X']:
                    total += roman[n] - roman[numeral]
                    i += 2
                elif numeral == 'X' and n in ['L', 'C']:
                    total += roman[n] - roman[numeral]
                    i += 2
                elif numeral == 'C' and n in ['D', 'M']:
                    total += roman[n] - roman[numeral]
                    i += 2
                else:
                    total += roman[numeral]
                    i += 1
            else:
                total += roman[numeral]
                i += 1

        return total
