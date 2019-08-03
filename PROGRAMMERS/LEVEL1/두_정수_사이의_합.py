def solution(a, b):
    answer = 0

    # a가 b보다 크면 둘이 바꿔주기
    if a > b:
        a, b = b, a

    for num in range(a, b+1):
        answer += num

    return answer


solution(3, 5)
solution(3, 3)
solution(5, 3)
