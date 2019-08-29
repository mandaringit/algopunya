import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())

    cities = list(map(int, input().split()))

    possible_move = D
    construct = 0

    for warp in cities:
        possible_move -= 1  # 도시 하나 이동시마다 가능한 움직임 -1

        # 거리보충
        if warp == 1:
            possible_move = D

        # 워프가 아니면
        else:
            # 아직 워프로 갈 수 있어
            if possible_move > 0:
                continue

            # 워프가 없으면 못가니 워프 짓고 거리보충
            elif possible_move == 0:
                construct += 1
                possible_move = D

    print("#{} {}".format(tc, construct))
