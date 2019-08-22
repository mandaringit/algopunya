import sys

sys.stdin = open('input.txt', 'r')


def rotate90(matrix):
    zip_matrix = list(zip(*matrix))

    rotate_matrix = []
    for row in zip_matrix:
        rotate_matrix.append(row[::-1])

    return rotate_matrix


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    r90 = rotate90(matrix)
    r180 = rotate90(r90)
    r270 = rotate90(r180)

    print(f"#{tc}")
    for i in range(N):
        print("".join(map(str, r90[i])), "".join(map(str, r180[i])), "".join(map(str, r270[i])))