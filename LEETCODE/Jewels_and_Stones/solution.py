import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        result = 0
        stone_counter = collections.Counter(S)

        for jewel in J:
            if jewel in stone_counter:
                result += stone_counter[jewel]

        return result
