# 단조증가수 여부
# 50개중 41개
# 4.17초
# 시간초과


def isSimpleIncrease(num):
    standard = int(str(num)[0])
    for i in str(num)[1:]:
        if int(i) < standard:
            return False
        else:
            standard = int(i)
    return True


T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = 0

    for idx, num in enumerate(numbers):
        if idx == len(numbers) - 1:
            break
        else:
            for next_idx in range(idx+1, len(numbers)):
                mul_num = num * numbers[next_idx]
                if isSimpleIncrease(mul_num):
                    if mul_num > max_num:
                        max_num = mul_num

    print(f"#{t} {max_num}")
