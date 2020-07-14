T = int(input())

for tc in range(1, T + 1):

    lines = list(map(int, input().split()))
    set_lines = set(lines)

    total = sum(set_lines)

    if len(set_lines) == 1:
        total *= 4
    else:
        total *= 2

    for i in lines:
        total -= i

    print(f"#{tc} {total}")
