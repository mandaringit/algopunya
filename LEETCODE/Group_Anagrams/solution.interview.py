from typing import List
import collections


class Solution:
    # 정렬한 뒤, 딕셔너리에 넣기
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict()
        for str in strs:
            anagrams[''.join(sorted(str))].append(str)

        return anagrams.values()
