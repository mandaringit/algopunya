N = int(input())
divisors = sorted([divisor for divisor in range(1, N+1) if N % divisor == 0])
for divisor in divisors:
    print(divisor, end=" ")
