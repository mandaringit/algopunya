import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

peoples = []

for _ in range(N):
    weight, height = map(int, input().split())
    rank = 1
    peoples.append([weight, height, rank])

comparison_set = []

for i in range(N):
    for j in range(N):
        if j != i and {i, j} not in comparison_set:  # 중복비교 없애기

            p1 = peoples[i]
            p2 = peoples[j]

            if p1[0] > p2[0] and p1[1] > p2[1]:
                peoples[j][2] += 1
            elif p1[0] < p2[0] and p1[1] < p2[1]:
                peoples[i][2] += 1

            comparison_set.append({i, j})

results = []

for _, __, rank in peoples:
    results.append(rank)

print(f"{' '.join(map(str, results))}")
