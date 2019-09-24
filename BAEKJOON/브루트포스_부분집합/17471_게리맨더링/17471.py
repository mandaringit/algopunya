import sys

sys.stdin = open('input.txt', 'r')


def check_area(subset):
    global N
    global populations
    global adj
    q = [subset[0]]
    visited = [0] * (N + 1)
    visited[subset[0]] = 1
    total_population = 0

    while q:
        x = q.pop(0)
        total_population += populations[x]

        for n in subset:
            # 방문 안했고,  인접해 있는거면 큐에 넣자
            if visited[n] == 0 and n in adj[x]:
                visited[n] = 1
                q.append(n)

    for i in subset:
        if visited[i] == 0:  # 끊김
            return 0

    return total_population


N = int(input())
populations = [0] + list(map(int, input().split()))
minV = 10000000000000

adj = {i: set() for i in range(1, N + 1)}

for i in range(1, N + 1):
    infos = list(map(int, input().split()))
    for node in infos[1:]:
        adj[i].add(node)
        adj[node].add(i)

# 두 구역으로 나누는 부분집합들 구하기
arr = [i for i in range(1, N + 1)]
for i in range(1, 1 << N // 2):
    subset1 = []
    subset2 = []
    for j in range(N):
        if i & (1 << j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])

    # 각 그룹탐색 , 인구 차이를 구함
    result1 = check_area(subset1)
    result2 = check_area(subset2)

    if result1 == 0 or result2 == 0:
        pass
    else:
        diff = abs(result1 - result2)
        if diff < minV:
            minV = diff

print(minV)
