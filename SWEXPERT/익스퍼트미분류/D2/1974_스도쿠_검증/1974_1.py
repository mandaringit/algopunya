def isValidate(set_line):
    validate = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    return set_line == validate


def sudokuCheck(sudoku):

    # 가로줄
    for row in sudoku:
        if not isValidate(set(row)):
            return 0

    # 세로줄
    zip_sudoku = list(zip(*sudoku))
    for column in zip_sudoku:
        if not isValidate(set(column)):
            return 0

    # 3 x 3 을 3개씩 잡아서 검사
    set1 = set()
    set2 = set()
    set3 = set()
    for idx, row in enumerate(sudoku):
        set1.update(row[:3])
        set2.update(row[3:6])
        set3.update(row[6:])
        if idx in [2, 5, 8]:
            if isValidate(set1) and isValidate(set2) and isValidate(set3):
                return 1
            else:
                return 0
            # 다음 3개 하기 전 초기화
            set1 = set()
            set2 = set()
            set3 = set()


T = int(input())

for t in range(1, T+1):
    sudoku = []
    for _ in range(9):
        sudoku.append(input().split())

    print(f"#{t} {sudokuCheck(sudoku)}")
