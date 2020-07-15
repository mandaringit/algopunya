# 뭐같은 문제
cycle = 0
given = input()
N = given
while True:
    cycle += 1
    N = str(N)
    if 0 < int(N) < 10:
        N = '0' + N

    elif int(N) == 0:
        # 이조건이 필수다 ㅠㅠ 슈발
        break

    step1 = str(int(N[0]) + int(N[1]))

    if len(step1) == 1:
        step1 = '0' + step1

    result = N[1] + step1[1]

    if int(result) == int(given):
        break

    N = int(result)
print(cycle)
