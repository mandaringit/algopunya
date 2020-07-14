import sys

sys.stdin = open('input.txt', 'r')


# 시간초과
def solution(stones, k):
    N = len(stones)
    minV = 2000000000

    next = 0
    while next + k <= N:
        max_stone = 0
        check = True
        temp_next = next + 1
        for ni in range(next, next + k):
            # 돌값이 최대보다 크면 돌 필요 없음
            if stones[ni] >= minV:
                temp_next = ni + 1
                check = False
                break
            elif stones[ni] > max_stone:
                max_stone = stones[ni]

        if check and minV > max_stone:
            minV = max_stone
        next = temp_next

    if minV == 2000000000:
        minV = 0

    return minV


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
