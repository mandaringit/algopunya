def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)

    return total


T = int(input())

results = []

for tc in range(1, T + 1):

    N = int(input())

    while len(str(N)) != 1:
        N = digit_sum(N)

    results.append(f"#{tc} {N}")

print("\n".join(results))
