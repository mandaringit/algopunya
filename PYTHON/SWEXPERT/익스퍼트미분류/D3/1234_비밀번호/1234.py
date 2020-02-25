import sys

sys.stdin = open('input.txt', 'r')


def remove_password(i, password):
    return password[:i] + password[i + 2:]


for tc in range(1, 11):

    N, password = input().split()

    start_idx = 0
    stop = False

    while not stop:

        pass_len = len(password)

        for i in range(start_idx, pass_len - 1):

            # 기본적으로 두개를 잡아서 비교한다.
            p1 = password[i]
            p2 = password[i + 1]

            # 같을때
            if p1 == p2:
                # 범위의 마지막 비교가 아닐때 그 다음 루프의 시작 인덱스를 제거한 인덱스 이전으로 변경
                if i != pass_len - 2:
                    password = remove_password(i, password)
                    start_idx = i - 1
                    # 탈출하고 변경 조건으로 다시 루프
                    break

                # 범위의 마지막 비교일때 제거 후 while 루프 중단
                else:
                    password = remove_password(i, password)
                    stop = True

            # 같지 않고 마지막 비교일때 더 바꿀게 없으니 while 루프 중단
            if p1 != p2 and i == pass_len - 2:
                stop = True

    print(f"#{tc} {password}")
