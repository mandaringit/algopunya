def solution(n, m):

    # 최대공약수
    gcd = 1

    for i in range(1, n + 1):
        if n % i == 0:
            if m % i == 0:
                gcd = i

    # 최소공배수 = 두수의 곱 / 최대공약수
    lcm = round((n * m) / gcd)

    return [gcd, lcm]


solution(3, 12)  # [3, 12]
solution(2, 5)  # [1,10]
