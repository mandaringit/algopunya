# 하샤드 수이려면, x % x의 자릿수의 합 == 0이어야 한다.


def solution(x):
    total = 0
    for snum in str(x):
        total += int(snum)

    return x % total == 0


solution(10)  # True
solution(12)  # True
solution(11)  # False
solution(13)  # False
