import sys

sys.stdin = open('input.txt', 'r')
# 시간 초과를 피하려면 deque를 사용.
from collections import deque

N = int(input())

cards = [num for num in range(1, N + 1)]
q = deque()

q.extend(cards)
while len(q) != 1:
    q.popleft()  # 버리고
    q.append(q.popleft())  # 빼서 바닥으로

print(q.popleft())
