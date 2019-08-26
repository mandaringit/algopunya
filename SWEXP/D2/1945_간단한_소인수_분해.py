T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = f"#{tc}"
    power_dict = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0
    }

    prime_factors = list(power_dict.keys())
    factor_idx = 0
    while N != 1:
        prime_factor = prime_factors[factor_idx]
        if N % prime_factor == 0:
            power_dict[prime_factor] += 1
            N = N // prime_factor
        else:
            factor_idx += 1

    for value in power_dict.values():
        result += f" {value}"

    print(result)
