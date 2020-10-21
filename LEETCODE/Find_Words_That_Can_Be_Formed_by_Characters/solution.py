from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        counter = Counter(chars)
        good_length = 0
        for word in words:
            is_good = True
            word_counter = Counter(word)
            for char in word_counter:
                if char in counter and counter[char] >= word_counter[char]:
                    pass
                else:
                    is_good = False
                    break

            if is_good:
                good_length += len(word)

        return good_length
