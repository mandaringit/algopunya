import sys

sys.stdin = open('input.txt', 'r')

N = int(input())  # 0 ~ 20
S = [list(map(int, input().split())) for _ in range(N)]

peoples = [i for i in range(N)]
min_diff = 100 * N
for i in range(1, (1 << N) // 2):
    team1 = []
    team2 = []
    for j in range(N):
        if i & (1 << j):
            team1.append(peoples[j])
        else:
            team2.append(peoples[j])

    S1 = 0
    S2 = 0
    for m in range(0, len(team1) - 1):
        for k in range(m + 1, len(team1)):
            S1 += S[team1[m]][team1[k]] + S[team1[k]][team1[m]]

    for m in range(0, len(team2) - 1):
        for k in range(m + 1, len(team2)):
            S2 += S[team2[m]][team2[k]] + S[team2[k]][team2[m]]

    diff = abs(S1 - S2)

    if diff < min_diff:
        min_diff = diff

print(min_diff)
