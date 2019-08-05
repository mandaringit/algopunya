# 월급을 상자에 담아서 준다.
# p_i 확률로 x_i 만원이 들어있다 .. 랜덤박스..

# 다솔이가 받을 수 있는 월급평균


def solution(N, p_i, x_i):
    total = 0
    for _ in range(N):
        total += float(p_i) * float(x_i)
    return total


T = int(input())
for t in range(T):
    N = int(input())
    p_i, x_i = input().split()
    answer = solution(N, p_i, x_i)
    print(f"#{t+1} {answer:.6f}")
