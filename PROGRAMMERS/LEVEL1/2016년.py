# 2016년 1월 1일은 금요일 , 윤년
# 2016년 a월 b일은 무슨요일?


def solution(a, b):
    answer = ''

    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]

    # 두 날짜의 차이를 구하자
    day_gap = 0

    # 마지막 월 제외, 월별로 더하고
    for month in range(1, a):
        if month in d31:
            day_gap += 31
        elif month in d30:
            day_gap += 30
        else:
            day_gap += 29

    # 마지막 월은 날로 비교해서 더해주자
    day_gap += (b - 1)

    # 1월 1일 기준 0번째 인덱스
    weeks = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    week_idx = day_gap % 7
    answer = weeks[week_idx]

    return answer


solution(5, 24)
