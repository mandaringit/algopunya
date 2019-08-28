import sys

sys.stdin = open('sample_input.txt', 'r')


def check_line(line, N, X):
    fake_road = [0] * N
    for i in range(0, N - 1):

        diff = abs(line[i] - line[i + 1])

        # 두개가 다르면
        if diff == 1:

            std = line[i]
            right = line[i + 1]

            # 왼쪽이 더 높을때, 도로건설은 i+1 부터 +1씩이다.
            if std > right and i + X < N:
                for x in range(i + 1, i + X + 1):
                    # 해당 라인의 x자리가 기준보다 높이가 다르거나, 이미 도로 건설안된곳.
                    if line[x] == right and fake_road[x] == 0:
                        fake_road[x] = 1
                    else:
                        return False


            # 오른쪽이 더 높을때 도로건설은 i부터 -1 씩이다
            elif std < right and 0 <= i + 1 - X:
                for x in range(i, i - X, -1):
                    if line[x] == std and fake_road[x] == 0:
                        fake_road[x] = 1
                    else:
                        return False
            else:
                return False
        # 같으면
        elif diff == 0:
            continue

        # 단차가 1 초과
        else:
            return False  # 불가능한 경우

    return True


T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for row in land:
        if check_line(row, N, X):
            count += 1

    col_land = list(zip(*land))

    for col in col_land:
        if check_line(col, N, X):
            count += 1

    print("#{} {}".format(tc, count))
