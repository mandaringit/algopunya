# 에라토스테네스의 체
def solution1(n):

    # 만약 n까지 포함이면 범위는 n+1
    # n 미포함이면 n
    r = n + 1

    # 일단 n+1 개의 수(0 ~ n) 모두 소수 = True라고 가정하고 출발
    prime_list = [True] * r

    # 루트(n) => 여기까지만 검사하면 된다.
    m = int(r**0.5)

    # 2 ~ m 까지 루프를 돌면서
    for i in range(2, m + 1):

        # 만약 소수리스트가 True면
        if prime_list[i] == True:

            # 해당 수의 다음 배수(i=2면, i+i = 4부터 n까지 i=2씩 증가시키면서)
            for j in range(i + i, r, i):

                # 소수리스트에서 해당 값들을 False로 바꾼다.
                prime_list[j] = False

    # 찾은 소수 리스트
    real_prime_list = [num for num in range(2, r) if prime_list[num] == True]

    return len(real_prime_list)  # 소수개수 리턴


solution1(10000)


#############


# 2 단순히 다 돌면서 찾기
def solution2(n):
    answer = 0

    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False

        if is_prime:
            answer += 1

    return answer


solution2(10000)
