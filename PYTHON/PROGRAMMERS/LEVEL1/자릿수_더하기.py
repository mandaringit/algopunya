def solution(n):
    answer = 0

    for snum in str(n):
        answer += int(snum)

    return answer


solution(987)  # 24
