import sys

sys.stdin = open('sample_input.txt', 'r')


def f(n, k, K, sv, vv):
    global maxV
    if n == k:
        if sv < K:
            if maxV < vv:
                maxV = vv
            return
    else:
        if sv == K:
            if maxV < vv:
                maxV = vv
            return
        elif sv > K:
            vv = vv - all[n - 1][1]
            if maxV < vv:
                maxV = vv
            return
        else:
            f(n + 1, k, K, sv, vv)
            f(n + 1, k, K, sv + all[n][0], vv + all[n][1])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 부피
    all = []
    for nc in range(N):
        V, C = map(int, input().split())  # 부피, 가치
        all.append([V, C])

    maxV = 0
    f(0, N, K, 0, 0)
    print(maxV)
