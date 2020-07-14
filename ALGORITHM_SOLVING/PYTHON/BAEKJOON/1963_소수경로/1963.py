import sys

sys.stdin = open('input.txt', 'r')


def get_prime_numbers(N):
    primes = [True] * (N + 1)

    m = int((N + 1) ** (1 / 2))

    for i in range(2, m + 1):
        if primes[i]:

            for j in range(i + i, N + 1, i):
                primes[j] = False

    return [i for i in range(1000, N + 1) if primes[i]]


def BFS(start):
    global visited
    global prime_check
    global target

    if start == target:
        return 0

    visited[start] = 1
    q = [start]

    while q:
        x = q.pop(0)

        str_x = str(x)

        for i in range(4):
            for j in range(10):
                if str_x[i] != str(j):
                    c_number = str_x[:i] + str(j) + str_x[i + 1:]
                    int_c_number = int(c_number)
                    if int_c_number > 1000 and prime_check[int_c_number] and visited[int_c_number] == 0:
                        if int_c_number == target:
                            return visited[x]
                        else:
                            visited[int_c_number] = visited[x] + 1
                            q.append(int_c_number)


    return 'Impossible'


T = int(input())

prime = get_prime_numbers(10000)

for tc in range(T):
    start, target = map(int, input().split())

    prime_check = [0] * 10000
    visited = [0] * 10000

    for num in prime:
        prime_check[num] = 1

    print(BFS(start))
