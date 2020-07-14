test_case = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for case_number in range(test_case):
    m1, d1, m2, d2 = tuple(map(int, input().split()))

    total = 0

    if m1 == m2:
        total = d2 - d1 + 1
    else:
        start_month_index = m1 - 1
        end_month_index = m2 - 1

        month_total = 0
        for month_index in range(start_month_index, end_month_index):
            month_total += days[month_index]

        day_gap = d2 - d1

        total = month_total + day_gap + 1

    print(f"#{case_number+1} {total}")

"""
#테스트 끄적

days = [31,28,31,30,31,30,31,31,30,31,30,31]

case = "3 1 4 31"

m1,d1,m2,d2 = tuple(map(int,case.split()))

# m1 == m2 일땐, d2 - d1 + 1 이 원하는 답.

# m1 != m2일땐,

start_month_index = m1 -1
end_month_index = m2 - 1

month_total = 0

for month_index in range(start_month_index,end_month_index):
    print(f"index => {month_index}, 실제 월 => {month_index+1}")
    month_total += days[month_index]
print(month_total)

day_gap = d2 - d1

total = month_total + day_gap + 1 # 1은 내가보기엔 당일을 포함..? 하는 느낌..? 첫번째 날짜의 1일째니까?
print(total)
"""
