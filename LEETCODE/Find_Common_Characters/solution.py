from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        std = Counter(A[0])

        for word in A[1:]:
            std &= Counter(word)

        return list(std.elements())
