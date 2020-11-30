class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        prime_count = 0

        for i in range(2, n):
            if is_prime[i]:  # 소수이면, 해당 수의 배수를 모두 False로 바꾼다.
                prime_count += 1
                for j in range(i + i, n, i):
                    is_prime[j] = False

        return prime_count
