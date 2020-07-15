# 753ms

# 소수 구하는 함수


def getPrimeList(N):
    primes = [True] * N

    m = int(N**(1 / 2))

    for i in range(2, m + 1):
        if primes[i]:
            for j in range(i + i, N, i):
                primes[j] = False

    return [i for i in range(2, N) if primes[i]]


T = int(input())

results = []

for t in range(1, T + 1):
    odd = int(input())
    possible_case = []

    # 소수를 구하고
    primes = getPrimeList(odd)

    # 큰수부터 돌면서
    for x in primes[::-1]:
        for y in primes:
            # 중복을 제외하기 위해 x보다 작거나 같은 수이면
            if y <= x:
                z = odd - (x + y)
                # z의 경우가 있는지 확인하고 넣자.
                if z in primes and z <= y:
                    possible_case.append([x, y, z])
            else:
                # 위의 범위를 벗어난 수 부터는 돌 필요가 없다
                break

    results.append(f"#{t} {len(possible_case)}")
print("\n".join(results))


# 822ms
"""prime_list = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]

T = int(input())

results = []

for t in range(1, T + 1):
    odd = int(input())

    answers = []

    this_prime_list = list(filter(lambda x: x < odd, prime_list))

    for x in this_prime_list[::-1]:
        for y in this_prime_list:
            if y <= x:
                z = odd - (x+y)
                if z in this_prime_list and z <= y:
                    answers.append([x, y, z])
            else:
                break
    results.append(f"#{t} {len(answers)}")
print("\n".join(results))"""


# 3533ms
"""prime_list = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]

T = int(input())

for t in range(1, T + 1):
    odd = int(input())

    answers = []

    this_prime_list = list(filter(lambda x: x < odd, prime_list))

    for x in this_prime_list[::-1]:
        for y in list(filter(lambda y: y <= x, this_prime_list)):
            z = odd - (x+y)
            if z in this_prime_list and z <= y:
                answers.append([x, y, z])
    print(f"#{t} {len(answers)}")
"""
