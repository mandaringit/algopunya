import sys

sys.stdin = open('sample_input.txt', 'r')


# 왜 더 느려..?

def DFS(operator_idx, number_idx, total, visited):
    global numbers, operators, maxV, minV

    visited[operator_idx] += 1

    if operator_idx == 0:
        total += numbers[number_idx]
    elif operator_idx == 1:
        total -= numbers[number_idx]
    elif operator_idx == 2:
        total *= numbers[number_idx]
    else:
        if total < 0:
            total = -total
            total //= numbers[number_idx]
            total = -total
        else:
            total //= numbers[number_idx]

    if visited[operator_idx] > operators[operator_idx]:
        return
    elif visited == operators:
        if total > maxV:
            maxV = total
        if total < minV:
            minV = total
    else:
        for i in range(4):
            DFS(i, number_idx+1, total, visited[:])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    maxV = -1000000000
    minV = 1000000000
    for i in range(4):
        DFS(i, 1, numbers[0], [0, 0, 0, 0])

    print("#{} {}".format(tc, maxV-minV))
