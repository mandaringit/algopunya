end_number = int(input())

for number in range(1, end_number+1):
    number_list = list(str(number))
    count_3 = number_list.count('3')
    count_6 = number_list.count('6')
    count_9 = number_list.count('9')
    total_clap = count_3 + count_6 + count_9
    if total_clap > 0:
        print(total_clap * "-", end=" ")
    else:
        print(number, end=" ")
