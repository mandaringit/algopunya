def solution(n):
    pow_numbers = []
    i = 0
    while 3 ** i <= 10 ** 10:
        pow_numbers.append(3 ** i)
        i += 1

    numbers = set(pow_numbers)
    N = len(pow_numbers)
    for i in range(1, 1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(pow_numbers[j])
        summation = sum(subset)
        numbers.add(summation)

    new_numbers = list(numbers)
    new_numbers.sort()

    return new_numbers[n-1]


print(solution(1))
