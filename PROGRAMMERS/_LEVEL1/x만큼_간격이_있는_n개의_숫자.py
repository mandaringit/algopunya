def solution(x, n):
    answer = []
    count = 0
    while count != n:
        count += 1
        answer.append(x * count)

    return answer


solution(4, 3)  # [4, 8, 12]
solution(-4, 2)  # [-4,-8]
