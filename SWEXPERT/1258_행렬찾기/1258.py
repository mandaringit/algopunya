import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    warehouse = [list(map(int, input().split())) for _ in range(N)]

    marking = [[0] * N for _ in range(N)]

    house_information = {}

    matrix_count = 0

    for i in range(N):
        for j in range(N):
            if warehouse[i][j] > 0 and marking[i][j] == 0:
                matrix_count += 1
                start = [i, j]
                end = [i, j]

                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    marking[x][y] = matrix_count
                    if end[0] < x:
                        end[0] = x
                    if end[1] < y:
                        end[1] = y

                    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                    for dx, dy in d:
                        ni = x + dx
                        nj = y + dy

                        if 0 <= ni < N and 0 <= nj < N:
                            if warehouse[ni][nj] and marking[ni][nj] == 0:
                                stack.append([ni, nj])

                height = end[0] - start[0] + 1
                width = end[1] - start[1] + 1
                size = width * height

                if size in house_information:
                    house_information[size].append([height, width])
                    house_information[size].sort(key=lambda h_i: h_i[0])
                else:
                    house_information[size] = [[height, width]]

    result = "#{} {}".format(tc, matrix_count)
    for size in sorted(list(house_information)):
        for height, width in house_information[size]:
            result += " {} {}".format(height, width)

    print(result)
