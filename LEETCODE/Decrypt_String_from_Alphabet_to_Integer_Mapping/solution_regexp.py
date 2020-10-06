import re


class Solution:
    def freqAlphabets(self, s):
        matched = re.findall(r'\d\d#|\d', s)
        return "".join(chr(int(i[:2]) + 96) for i in matched)
