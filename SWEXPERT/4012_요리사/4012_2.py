import sys

sys.stdin = open('sample_input.txt', 'r')


def checkS(group):
    global S
    L = len(group)
    totalS = 0
    for i in range(L-1):
        for j in range(i+1, L):
            totalS += S[group[i]][group[j]]+S[group[j]][group[i]]

    return totalS


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    minDiff = 100000000
    gradient = [i for i in range(N)]
    for i in range(1, (1 << N)//2):
        group1 = []
        group2 = []
        for j in range(N):
            if i & (1 << j):
                group1.append(gradient[j])
            else:
                group2.append(gradient[j])

        # 반띵일때만
        if len(group1) == N//2:
            S1 = checkS(group1)
            S2 = checkS(group2)

            diff = abs(S1-S2)
            if diff < minDiff:
                minDiff = diff

    print("#{} {}".format(tc, minDiff))
