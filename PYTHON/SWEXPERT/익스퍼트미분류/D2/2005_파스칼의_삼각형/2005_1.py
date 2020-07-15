case_number = int(input())

for loop_number in range(case_number):
    N = int(input())

    start_line = []

    print(f"#{loop_number + 1}")
    for i in range(N):

        if i >= 2:
            # 새로 넣을 리스트 만들고
            next_line = []

            for idx, num in enumerate(start_line):
                # 마지막 인덱스가 아니면
                if idx != len(start_line)-1:
                    # 옆 인덱스 숫자랑 더해서 새로 넣을 라인에 추가
                    add_num = num + start_line[idx+1]
                    next_line.append(add_num)

            # N번째 라인의 중간부분만 변경
            start_line[1:i] = next_line

        # 공통, 마지막에 1을 추가
        start_line += [1]
        print(f"{start_line}".replace(
            "[", "").replace("]", "").replace(",", ""))

# 프린트 더럽넹...
