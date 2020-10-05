class Solution:
    def toLowerCase(self, str: str) -> str:
        result = []
        for char in str:
            ascii_num = ord(char)
            if 65 <= ascii_num <= 90:
                result.append(chr(ascii_num+32))
            else:
                result.append(char)

        return "".join(result)
