import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 청소한 영역

# 북 동 남 서 순서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
turning = {
    (-1, 0): [3, 2, 1, 0],  # d=0 북
    (0, 1): [0, 3, 2, 1],  # d=1 동
    (1, 0): [1, 0, 3, 2],  # d=2 남
    (0, -1): [2, 1, 0, 3]  # d=3 서
}

clean_count = 0

while True:
    # 1. 현재 위치를 청소합니다. => 로봇은 청소 했던 곳을 또 청소하지 않습니다!
    if visited[r][c] != 1:
        visited[r][c] = 1
        clean_count += 1
    # 2. 현재 위치에서 현재방향 기준 왼쪽방향부터 탐색합니다.
    current_direction = directions[d]
    turning_seq = turning[current_direction]
    is_all_clean = True
    for seq in turning_seq:
        dx, dy = directions[seq]
        ni = r + dx
        nj = c + dy

        # 인덱스 밖이 아니고,
        if 0 <= ni < N and 0 <= nj < M and area[ni][nj] != 1:
            # 청소도 안되어 있다면 = 방문 안했으면
            if visited[ni][nj] != 1:
                d = seq  # 그방향으로 회전한 다음
                r, c = ni, nj  # 한칸 전진.
                is_all_clean = False
                break

    # 만약 모두 청소되어있는 경우
    if is_all_clean:
        dx, dy = -current_direction[0], -current_direction[1]  # 반대방향
        ni = r + dx
        nj = c + dy

        if 0 <= ni < N and 0 <= nj < M and area[ni][nj] != 1:
            r, c = ni, nj  # 방향 유지한채 후진
        else:
            # 작동 정지
            break

print(clean_count)
