# 입력 : 축구에 참여하는 인원 N, 이후부터 N개의 줄에 S.
# 출력 : 두 팀으로 나눴을때, 두 팀의 S의 차이가 최소가 될때의 값
# 접근 : 팀을 절반으로 나누는 모든 경우의 수를 구한다 -> 각 경우마다 S의 차이를 구해 비교.
import sys

sys.stdin = open('input.txt', 'r')


def get_synergy(team):
    global S
    global N
    total_synergy = 0

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            p1 = team[i] - 1
            p2 = team[j] - 1
            total_synergy += S[p1][p2]
            total_synergy += S[p2][p1]

    return total_synergy


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
peoples = [i for i in range(1, N + 1)]
min_diff = 200 * (N // 2)
for i in range(1, (1 << N) // 2):
    team1 = []
    team2 = []
    for j in range(N):
        if i & (1 << j):
            team1.append(peoples[j])
        else:
            team2.append(peoples[j])

    if len(team1) == N // 2:
        t1_s = get_synergy(team1)
        t2_s = get_synergy(team2)
        diff = abs(t1_s - t2_s)

        if diff < min_diff:
            min_diff = diff

print(min_diff)
