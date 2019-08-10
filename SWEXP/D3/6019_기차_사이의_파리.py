T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())

    strike_time = D / (A+B)
    fly_distance = strike_time*F

    print(f"#{t} {fly_distance}")
