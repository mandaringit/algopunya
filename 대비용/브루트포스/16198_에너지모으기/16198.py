import sys

sys.stdin = open('input.txt', 'r')


def DFS(next_energies, total):
    global maxE

    if len(next_energies) == 2:
        if total > maxE:
            maxE = total
    else:
        for x in range(1, len(next_energies) - 1):
            new_energies = next_energies[:x] + next_energies[x + 1:]
            next_total = total + next_energies[x - 1] * next_energies[x + 1]
            DFS(new_energies, next_total)


N = int(input())
energies = list(map(int, input().split()))
maxE = 0
for i in range(1, N - 1):  # 첫번째, 마지막 제외
    start_e = energies[i - 1] * energies[i + 1]
    new_energies = energies[:i] + energies[i + 1:]
    DFS(new_energies, start_e)

print(maxE)