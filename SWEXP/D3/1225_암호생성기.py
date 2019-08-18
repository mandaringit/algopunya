for tc in range(1, 11):
    tc_num = int(input())

    codes = list(map(int, input().split()))

    decrease_number = [1, 2, 3, 4, 5]
    decrease_idx = 0
    while True:
        # 0번째 추출
        first_number = codes.pop(0)

        first_number -= decrease_number[decrease_idx]

        if first_number < 0:
            first_number = 0

        # 뒤에 붙이기
        codes.append(first_number)

        if first_number == 0:
            break
        else:
            decrease_idx = (decrease_idx + 1) % 5

    print(f"#{tc} {' '.join(map(str, codes))}")
