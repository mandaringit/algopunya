import sys

sys.stdin = open('sample_input.txt', 'r')


def is_range_ok(i, j):
    return 0 <= i < N and 0 <= j < N


def get_caffe(points):
    global stores
    d = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    i, j = points[0]
    path = [stores[i][j]]
    i += 1
    j += 1
    d_idx = 0
    while (i, j) != points[0]:

        value = stores[i][j]
        if value not in path:
            path.append(value)
        else:
            return -1

        if (i, j) in points:
            d_idx += 1

        i += d[d_idx][0]
        j += d[d_idx][1]

    return len(path)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stores = [list(map(int, input().split())) for _ in range(N)]

    maxPath = -1
    # 시작점 선택
    for i1 in range(0, N - 1):
        for j1 in range(1, N - 1):

            # 두번째 점 선택
            for d1 in range(1, N):
                i2 = i1 + (1 * d1)
                j2 = j1 + (1 * d1)
                if is_range_ok(i2, j2):

                    # 세번째 점 선택
                    for d2 in range(1, N):
                        i3 = i2 + (1 * d2)
                        j3 = j2 + (-1 * d2)
                        if is_range_ok(i3, j3):

                            # 4번째 점 확정
                            i4 = i3 + (-1 * d1)
                            j4 = j3 + (-1 * d1)
                            if is_range_ok(i4, j4):
                                path_length = get_caffe([(i1, j1), (i2, j2), (i3, j3), (i4, j4)])

                                if path_length > maxPath:
                                    maxPath = path_length

    print("#{} {}".format(tc, maxPath))
