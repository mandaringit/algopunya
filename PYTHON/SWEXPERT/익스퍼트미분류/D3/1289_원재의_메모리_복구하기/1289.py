T = int(input())

for tc in range(1, T + 1):
    original = input()

    count = 0
    change_bit = ['1', '0']  # 모든게 0부터 시작하므로 1부터 찾는다.
    c_bit_idx = 0

    for bit in original:

        if bit == change_bit[c_bit_idx]:
            count += 1
            # 1을 찾았으면 그다음엔 0이나오는걸 찾고 그다음엔 1이나오는걸 찾고..
            c_bit_idx = (c_bit_idx + 1) % 2

    print(f"#{tc}", count)


'''
원본이 01100 이라면, 0000에서 시작해서 가다가 1인걸 찾는다.
두번째 에서 멈춰서 01111로 바꾸고, 그다음엔 0으로 바꿀걸 찾는다.
01100 이렇게 바꾸면 끝.

즉, 돌면서 1을 찾고, 찾으면 카운팅후 그다음엔 0을 찾는다.
그렇게 0을 찾으면 카운팅 후 다음엔 1을 찾는다. 이 과정을 반복
'''
