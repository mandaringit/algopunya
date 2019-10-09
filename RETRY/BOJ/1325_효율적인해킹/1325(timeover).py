import sys

sys.stdin = open('input.txt', 'r')


# 시간초과. 값을 저장하면서 가는 방법을 생각해보던지 해야겠다.
# 단방향 이므로 하위 노드들을 한번 지나갔으면, 그 노드의 값은 이미 구해진거나 마찬가지라고 생각하고 풀어야 할 것 같다.

def BFS(start):
    global belief

    visited = {start}
    stack = [start]

    while stack:
        c = stack.pop()

        for computer in belief[c] - visited:
            visited.add(computer)
            stack.append(computer)

    return len(visited)


N, M = map(int, input().split())  # N computer , M relation

belief = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    c1, c2 = map(int, input().split())

    # c1 trust c2. one direction.
    belief[c2].add(c1)

maxV = 0
computers = []
for i in range(1, N + 1):
    length = BFS(i)
    if length > maxV:
        maxV = length
        computers = [i]

    elif length == maxV:
        computers.append(i)

print("{}".format(' '.join(map(str, computers))))
