import sys

sys.stdin = open('input.txt', 'r')


def DFS(i, summation, last, used):
    global numbers, K, N, count
    summation += numbers[i]
    used[i] += 1
    last -= numbers[i]

    if summation == K:
        count += 1
    elif summation > K:
        return
    elif last + summation < K:
        return
    else:
        for k in range(N):
            if not used[k]:
                DFS(k, summation, last, used[:])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(sorted(list(map(int, input().split()))))
    total = sum(numbers)
    used = [0] * N
    count = 0
    for i in range(N):
        DFS(i, 0, total, used)
    print(f"#{tc} {count}")
