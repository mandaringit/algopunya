from collections import Counter, defaultdict
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 단어 문자가 아닌 것들을 ' '로 치환 후 소문자화, 분리 후 금지어인지 아닌지 판단.
        words = [word for word in re.sub(
            '[^\w]', ' ', paragraph).lower().split() if word not in banned]

        """ using default dict
        counter = defaultdict(words)
        for word in words:
            counter[word] += 1
        
        return max(counter,key=counter.get)
        """
        counter = Counter(words)

        return counter.most_common(1)
