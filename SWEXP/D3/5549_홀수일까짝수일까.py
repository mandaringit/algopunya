def isOddOrEven(N):
    return 'Odd' if N % 2 else 'Even'


T = int(input())

for t in range(1, T+1):
    case = int(input())
    print(f"#{t} {isOddOrEven(case)}")
