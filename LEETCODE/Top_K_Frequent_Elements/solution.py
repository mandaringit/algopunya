from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num[0] for num in counter.most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # 기본이 최소힙 & 튜플의 맨 앞의 요소로 정렬함
        # 때문에 최대힙으로 바꾸기 위해선 -를 붙여야함.
        max_heap = [(-freq, value) for value, freq in counter.items()]
        heapq.heapify(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(k)]
