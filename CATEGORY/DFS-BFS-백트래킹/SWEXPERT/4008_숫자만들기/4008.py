import sys

sys.stdin = open('sample_input.txt', 'r')


# 자칫 순열처럼 보일 순 있지만, 연산자가 겹치는게 많아 비효율적이다.
# 어차피 중간에 들어갈 경우는 +-*/ 네가지뿐이므로 모든경우를 만들어보고
# 연산자 수가 맞는 것들만 계산해서 비교해주면 된다.

def dfs(i, n_idx, path, total):
    global ops, ops_count, maxV, minV

    # 필요한 연산들
    if i == 0:
        total += numbers[n_idx]
    elif i == 1:
        total -= numbers[n_idx]
    elif i == 2:
        total *= numbers[n_idx]
    elif i == 3:
        if total < 0:
            total = -total // numbers[n_idx]
            total = -total
        else:
            total //= numbers[n_idx]

    path[i] += 1

    # 연산 후 해당 연산자가 적정 수라면
    if path[i] <= ops[i] and n_idx <= ops_count:

        # 연산자 수가 동일하다면
        if path == ops:
            if total < minV:
                minV = total
            if total > maxV:
                maxV = total
        else:
            for ni in range(4):
                dfs(ni, n_idx + 1, path[:], total)
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ops = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    ops_count = sum(ops)
    maxV = -100000000
    minV = 1000000000
    for i in range(4):
        dfs(i, 1, [0, 0, 0, 0], numbers[0])

    print(f"#{tc} {maxV - minV}")
