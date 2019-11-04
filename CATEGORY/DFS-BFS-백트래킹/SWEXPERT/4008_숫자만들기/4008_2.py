import sys

sys.stdin = open('sample_input.txt', 'r')


def DFS(i, total, count, used):
    global numbers, ops, maxV, minV

    if i == 0:
        total += numbers[count]
    elif i == 1:
        total -= numbers[count]
    elif i == 2:
        total *= numbers[count]
    elif i == 3:
        if total < 0:
            total = -total // numbers[count]
            total = -total
        else:
            total //= numbers[count]

    used[i] += 1

    if used[i] > ops[i]:
        return
    elif used == ops:
        if total > maxV:
            maxV = total
        if total < minV:
            minV = total
    else:
        for ni in range(4):
            DFS(ni, total, count + 1, used[:])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ops = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    maxV = -1000000000000
    minV = 1000000000000
    for i in range(4):
        DFS(i, numbers[0], 1, [0, 0, 0, 0])

    print(f"#{tc} {maxV - minV}")
