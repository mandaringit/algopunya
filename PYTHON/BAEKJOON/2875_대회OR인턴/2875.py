import sys

sys.stdin = open('input.txt','r')

N, M, K = map(int, input().split())
girl_team, girl_last = divmod(N, 2)
man_team, man_last = divmod(M, 1)
team_max = min(girl_team, man_team)
last = N - 2 * team_max + M - team_max

while last < K:
    team_max -= 1
    last = N - 2 * team_max + M - team_max
print(team_max)