def my_pow(number, power):
    if power <= 0:
        return 1
    else:
        return number * my_pow(number, power - 1)


for tc in range(1, 11):
    tc_num = int(input())

    number, power = map(int, input().split())

    print(f"#{tc} {my_pow(number,power)}")
