import sys

sys.stdin = open('input.txt', 'r')


def is_sudoku_valid(sudoku):
    valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 세로줄검사
    sudoku_column = zip(*sudoku)
    for col in sudoku_column:
        if set(col) != valid:
            return 0

    grid1 = set()
    grid2 = set()
    grid3 = set()

    # 가로줄 + 격자검사
    for i in range(0, len(sudoku)):

        # 가로줄검사
        if set(sudoku[i]) != valid:
            return 0

        # 격자 검사 (3개씩)
        grid1.update(sudoku[i][:3])
        grid2.update(sudoku[i][3:6])
        grid3.update(sudoku[i][6:])

        # 3번째줄, 6번째 줄, 9번째 줄만 검사
        if i in [2, 5, 8]:
            if grid1 != valid or grid2 != valid or grid3 != valid:
                return 0
            else:
                grid1 = set()
                grid2 = set()
                grid3 = set()

    return 1


T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f"#{tc} {is_sudoku_valid(sudoku)}")
