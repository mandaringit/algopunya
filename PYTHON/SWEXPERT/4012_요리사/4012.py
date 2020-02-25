import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    synergies = [list(map(int, input().split())) for _ in range(N)]
    foods = [i for i in range(N)]

    minV = 20000 * N

    for i in range(1 << N):
        grad1 = []
        grad2 = []

        for j in range(N):
            if i & (1 << j):
                grad1.append(foods[j])
            else:
                grad2.append(foods[j])

            if len(grad1) > N // 2 or len(grad2) > N // 2:
                break

        if len(grad1) == N // 2:
            food1_S = 0
            food2_S = 0

            for k in range(0, N // 2 - 1):
                for m in range(k + 1, N // 2):
                    a, b = grad1[k], grad1[m]
                    c, d = grad2[k], grad2[m]
                    food1_S += synergies[a][b] + synergies[b][a]
                    food2_S += synergies[c][d] + synergies[d][c]

            diff = abs(food1_S - food2_S)

            if diff < minV:
                minV = diff

    print("#{} {}".format(tc, minV))
