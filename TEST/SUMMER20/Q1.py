def solution(p):
    # 특정 연도 p -> 해당 연도보다 큰 아름다운 연도 중, 가장 작은 아름다운 연도?
    def is_beautiful_number(number):
        str_number = str(number)
        number_set = set(str_number)
        return len(number_set) == len(str_number)

    year = p + 1
    while not is_beautiful_number(year):
        year += 1

    return year


print(solution(1987))


