import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    # N은 페이지 개수 M은 원하는 페이지의 위치
    N, M = map(int, input().split())

    prs = list(map(int, input().split()))

    # 우선순위 , 위치 순
    priority_q = [(pr, i) for i, pr in enumerate(prs)]
    q = deque()

    q.extend(priority_q)

    prs.sort()
    printing_count = 0

    while q:
        priority, i = q.popleft()

        if priority == prs[-1]:
            prs.pop()
            printing_count += 1
            if i == M:
                break
        else:
            q.append((priority, i))

    print(printing_count)
