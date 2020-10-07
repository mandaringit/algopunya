class Solution:
    def sortString(self, s: str) -> str:

        chars = {chr(i): 0 for i in range(97, 97 + 26)}
        for char in s:
            chars[char] += 1

        result = []
        ASC = True
        while True:
            chracters = chars.keys() if ASC else reversed(list(chars.keys()))
            for key in list(chracters):
                if chars[key] > 0:
                    result.append(key)
                chars[key] -= 1
                if chars[key] <= 0:
                    del chars[key]

            ASC = ASC ^ 1
            if not chars:
                break

        return "".join(result)
