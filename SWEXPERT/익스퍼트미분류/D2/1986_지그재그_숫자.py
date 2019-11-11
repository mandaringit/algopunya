test_case = int(input())

for case_number in range(test_case):
    N = int(input())

    total = 0
    for i in range(1, N+1):
        total = total + i if i % 2 else total - i

    print(f"#{case_number + 1} {total}")
