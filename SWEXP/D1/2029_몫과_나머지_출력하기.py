case_num = int(input())

for loop_num in range(case_num):
    a, b = (int(number) for number in input().split())
    result = divmod(a, b)
    print(f"#{loop_num+1} {result[0]} {result[1]}")
