T = int(input())

result = []

for tc in range(1, T + 1):
    a_win, a_case, b_win, b_case = map(int, input().split())

    a_rate = a_win / a_case

    b_rate = b_win / b_case

    ans = f"#{tc} "

    if a_rate > b_rate:
        ans += 'ALICE'
    elif a_rate < b_rate:
        ans += 'BOB'
    else:
        ans += 'DRAW'

    result.append(ans)

print("\n".join(result))
