T = int(input())


def get_prime_numbers(N):
    primes = [True] * (N + 1)

    m = int((N + 1) ** (1 / 2))

    for i in range(2, m + 1):
        if primes[i]:

            for j in range(i + i, N + 1, i):
                primes[j] = False

    return [i for i in range(2, N + 1) if primes[i]]


primes = get_prime_numbers(1000000)

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    count = 0

    strD = str(D)
    idx = 0

    while True:
        if idx == len(primes) or primes[idx] > B:
            break

        if primes[idx] >= A and strD in str(primes[idx]):
            count += 1

        idx += 1

    print(f"#{tc} {count}")
