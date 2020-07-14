T = int(input())
for case_count in range(T):
    a, b = tuple(map(int, input().split()))
    print(f"Case #{case_count+1}: {a+b}")
