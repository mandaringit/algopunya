# n이 어떤 정수 x의 제곱인지 판단해보자.


def solution(n):
    answer = 0

    x = n**(1 / 2)

    # x가 정수인지 판단 => 소수라면 같을 수 없음
    # 123 == 123.1 => False
    if int(x) == x:
        # n이 정수 x의 제곱이라면 x+1의 제곱을 리턴
        return (x + 1)**2
    else:
        # 아니라면 -1을 리턴
        return -1


solution(121)  # 144 => 144.0 도 맞는듯
