# 리스트 컴프리헨션 보다 맵을 쓰면 좀더 빨라진다
case_number = int(input())

for case_num in range(case_number):

    possible_day = int(input())
    profit_sum = 0
    price_list = list(map(int, input().split()))

    max_number = max(price_list)
    big_index = price_list.index(max_number)

    while big_index < len(price_list):

        for i in range(big_index):
            profit = price_list[big_index] - price_list[i]
            profit_sum += profit

        price_list = price_list[big_index+1:]

        if not price_list:
            break
        else:
            max_number = max(price_list)
            big_index = price_list.index(max_number)

    print(f"#{case_num+1} {profit_sum}")
"""
case_number = 1

profit_sum = 0

for case_num in range(case_number):
    possible_day = 3
    
    price_list = [3,5,9]
    
    # 가장 큰 값의 인덱스를 구하고,
    max_number = max(price_list)
    big_index = price_list.index(max_number)
    
    while big_index<len(price_list):
        print(f"가격 리스트 => {price_list}")
        print(f"가장큰 수 => {max_number}")
        print(f"그 큰 수의 인덱스 =>{big_index}")
        # 그 값의 인덱스 전에 작은 값들이 있으면 그 차이를 더해서 누적.
        
        for i in range(big_index):
            profit = price_list[big_index] - price_list[i]
            profit_sum += profit

        # 다 끝났으면 그 큰 값의 인덱스 다음 인덱스부터 그다음 큰 값을 찾는다.
        price_list = price_list[big_index+1:]
        if not price_list :
            break
        else:
            max_number = max(price_list)
            big_index = price_list.index(max_number)

print(profit_sum)
"""
