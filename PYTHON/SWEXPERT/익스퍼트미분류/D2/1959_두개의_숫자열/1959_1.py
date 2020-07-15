test_case = int(input())

for case_number in range(test_case):
    A_len, B_len = (int(num) for num in input().split())
    if A_len >= B_len:
        fix = [int(num) for num in input().split()]
        move = [int(num) for num in input().split()]
    else:
        move = [int(num) for num in input().split()]
        fix = [int(num) for num in input().split()]

    max_sum = -float('inf')

    while len(move) != len(fix) + 1:
        zip_list = list(zip(move, fix))
        zip_total = 0

        for tp in zip_list:
            zip_total += tp[0] * tp[1]

        if zip_total > max_sum:
            max_sum = zip_total
        move.insert(0, 0)

    print(f"#{case_number+1} {max_sum}")


# 테스트 끄적

"""
# 길이 비교를 통해 작은놈을 선택하고, 그놈을 움직이여함
len_A = 3
len_B = 5

A = [1,5,3]
B = [3,6,-7,5,4]

print(list(zip(A,B)))
"""
"""
A = [1,5,3]
B = [3,6,-7,5,4]
max_sum = -float('inf')
while len(A) != len(B) + 1:
    zip_list = list(zip(A,B))
    print(zip_list)
    zip_total = 0

    for tp in zip_list:
        zip_total += tp[0] * tp[1]
    print(zip_total)
    if zip_total > max_sum:
        max_sum = zip_total
    A.insert(0,0)
print(max_sum)
"""
