import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)  # 최소힙화

        # 길이가 K가 될 때까지 작은 값들을 빼버림 -> 큰거 K개만 남음
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        # 지금 최소힙 길이가 k보다 작으면 최소힙에 삽입.
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)

        # 길이가 k보다 크고, 넣는 값이 최솟값보다 크다면
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)  # 최솟값과 넣는 값을 서로 교체

        # 이렇게 함으로써 최소힙의 가장 작은값이 K번째 큰 값이 된다.
        return self.pool[0]
