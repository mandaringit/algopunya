from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # 키가 큰 순(-h)으로 정렬. 동일하다면 k로 비교후 정렬 O(NlogN)
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []

        for p in people:
            res.insert(p[1], p)

        return res
