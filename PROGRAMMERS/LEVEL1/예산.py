# d = 부서별로 신청한 금액이 들어있는 배열
# budget = 예산


def solution(d, budget):
    d.sort()

    count = 0

    # 신청 금액이 적은놈부터 차례대로 나눠준다
    for money in d:
        if money <= budget:
            count += 1
            budget -= money

    return count


solution([1, 3, 2, 5, 4], 9)
solution([2, 2, 3, 3], 10)
