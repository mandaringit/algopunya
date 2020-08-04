def solution(n):
    word = '수박'

    if n > 2:
        Q, R = divmod(n, 2)
        if R:
            return word * Q + word[:1]
        else:
            return word * Q
    else:
        return word[:n]


print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))


# 옛날에 푼거

def solution2(n):
    answer = ''

    rest = n % 2

    if rest == 0:
        answer = '수박'*int((n/2))
    else:
        answer = '수박'*int(((n-1)/2))+"수"

    return answer
