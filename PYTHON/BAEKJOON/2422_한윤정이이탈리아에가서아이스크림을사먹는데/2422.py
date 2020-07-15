import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
bad = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    n1, n2 = map(int, input().split())
    bad[min(n1, n2)].append(max(n1, n2))

count = 0
for i in range(1, N - 1):
    for j in range(i + 1, N):
        if j not in bad[i]:
            for k in range(j + 1, N + 1):
                if k not in bad[i] and k not in bad[j]:
                    count += 1

print(count)
