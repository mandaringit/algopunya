# 줄여본거
def rotate90(array):
    # 묶고 뒤집으면 회전완료
    zip_column = list(zip(*array))

    rotate_array = [list(reversed(list(row))) for row in zip_column]

    return rotate_array


T = int(input())

for t in range(1, T+1):
    N = int(input())

    array = []
    for _ in range(N):
        array.append(input().split())

    r90 = rotate90(array)
    r180 = rotate90(r90)
    r270 = rotate90(r180)

    print(f"#{t}")
    # row 한줄씩 출력
    for i in range(N):
        print("".join(r90[i]), "".join(r180[i]), "".join(r270[i]))


# 첫풀이
"""
def rotate90(array):
    zip_column = list(zip(*array))

    rotate_array = []

    for row in zip_column:
        row = list(map(str, row))
        row.reverse()
        rotate_array.append(row)

    return rotate_array


def print_all(allarray,N):
    result = ""

    for i in range(N):
        line = ""
        for array in allarray:
            line += "".join(array[i]) + " "
        line.rstrip()
        result += line + "\n"

    return result.rstrip("\n")

T = int(input())

for t in range(1, T+1):
    N = int(input())

    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))

    r90 = rotate90(array)
    r180 = rotate90(r90)
    r270 = rotate90(r180)

    result = print_all([r90, r180, r270],N)

    print(f"#{t}\n{result}")
"""
