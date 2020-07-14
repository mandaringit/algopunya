import sys

sys.stdin = open('input.txt', 'r')


def solution(board, moves):
    # 넣을 바구니
    basket = []
    # 커맨드 실행
    count = 0
    for move in moves:  # move - 1 이 원하는 열이다.

        for i in range(len(board)):
            if board[i][move - 1] > 0:
                # 뽑기
                target = board[i][move - 1]
                board[i][move - 1] = 0

                # 넣기 (스택)
                if len(basket) > 0:
                    basket_last = basket[-1]
                    if basket_last == target:
                        basket.pop()
                        count += 2
                    else:
                        basket.append(target)
                else:
                    basket.append(target)
                break

    return count


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])
)