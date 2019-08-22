test_case = int(input())

for case_number in range(test_case):
    # 돈 인풋값의 맨 뒤가 0이 아닌게 있다고 하므로
    # 맨 마지막 숫자를 0으로 변경해주기
    money = input()
    money = money[:-1] + "0"
    money = int(money)
    money_count = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }
    while money != 0:
        for typ in money_count:
            if money >= typ:
                money -= typ
                money_count[typ] += 1
                break
    result = f"#{case_number+1}\n"
    for count in money_count.values():
        result += str(count) + " "
    print(result)


# 테스트 끄적

"""
money = 32850

money_count = {
    50000:0,
    10000:0,
    5000:0,
    1000:0,
    500:0,
    100:0,
    50:0,
    10:0
}

print(money_count)
while money != 0:
    if money >= 50000:
        money -= 50000
        money_count[50000] +=1
    elif money >= 10000:
        money -= 10000
        money_count[10000] +=1
    elif money >= 5000:
        money -= 5000
        money_count[5000] +=1
    elif money >= 1000:
        money -= 1000
        money_count[1000] +=1
    elif money >= 500:
        money -= 500
        money_count[500] +=1
    elif money >= 100:
        money -= 100
        money_count[100] +=1
    elif money >= 50:
        money -= 50
        money_count[50] += 1
    else :
        money -= 10
        money_count[10] += 1
print(money_count)
"""
