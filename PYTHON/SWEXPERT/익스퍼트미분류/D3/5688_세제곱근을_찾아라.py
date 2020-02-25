import math

T = int(input())

for t in range(1, T+1):
    N = int(input())

    result = -1

    root3 = N**(1/3)
    round_root3 = round(root3)

    if math.isclose(round_root3, root3):
        result = round_root3

    print(f"#{t} {result}")
