test_case = int(input())

for case_number in range(test_case):
    h1, m1, h2, m2 = (int(num) for num in input().split())

    calc_h = 0
    calc_m = 0

    calc_m += (m1 + m2)

    if calc_m >= 60:
        calc_h += 1
        calc_m -= 60

    calc_h += (h1 + h2)

    if calc_h >= 24:
        calc_h -= 24
    elif calc_h >= 12:
        calc_h -= 12

    if calc_h == 0:
        calc_h = 12

    print(f"#{case_number+1} {calc_h} {calc_m}")
