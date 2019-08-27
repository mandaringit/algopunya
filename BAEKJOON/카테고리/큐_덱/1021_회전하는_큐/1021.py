import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())

pick_card = list(map(int, input().split()))

numbers = [i for i in range(1, N + 1)]

q = deque(numbers)

pick_idx = 0

save = []

op1 = 0
op2 = 0
op3 = 0

while save != pick_card:

    if q[0] == pick_card[pick_idx]:
        save.append(q.popleft())
        op1 += 1
        pick_idx += 1

    else:
        # 앞에서 뺄지, 뒤에서 뺄지 위치를 파악해 거리를보고 결정해야
        # 최소로 연산을 수행 가능하다.

        location = q.index(pick_card[pick_idx])
        far_from_last = len(q) - location

        if location > far_from_last:
            q.appendleft(q.pop())
            op3 += 1
        else:
            q.append(q.popleft())
            op2 += 1

print(op2 + op3)
