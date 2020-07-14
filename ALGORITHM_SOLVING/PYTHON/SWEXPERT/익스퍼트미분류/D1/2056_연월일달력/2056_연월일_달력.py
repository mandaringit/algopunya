for loop_number in range(int(input())):
    date = input()
    # 스트링을 날짜로 구분
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    valid = f"#{loop_number+1} {date[:4]}/{date[4:6]}/{date[6:]}"
    invalid = f"#{loop_number+1} -1"

    # 형변환
    month = int(month)
    day = int(day)

    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]

    if month == 2:
        print(valid if 0 < day <= 28 else invalid)
    elif month in day_31:
        print(valid if 0 < day <= 31 else invalid)
    elif month in day_30:
        print(valid if 0 < day <= 30 else invalid)
    else:
        print(invalid)
