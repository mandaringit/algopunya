import collections
from typing import Deque
import re


class Solution:
    # 덱으로 양쪽에서 뽑아내면서 비교하는 방법.
    def isPalindrome(self, s: str) -> bool:
        # strs = []
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            # if strs.pop(0) != strs.pop():
            if strs.popleft() != strs.pop():
                return False

        return True

    # 슬라이싱 & 정규식
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
