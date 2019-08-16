N = 1000000

primes = [True] * N

m = int(N ** (1 / 2))

for i in range(2, m):
    if primes[i]:
        for j in range(i + i, N, i):
            primes[j] = False

primes_list = [str(i) for i in range(2, N) if primes[i]]

print(" ".join(primes_list))
