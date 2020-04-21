def solution(board, moves):
    result = 0
    basket = []
    N = len(board)

    for col in moves:
        for row in range(N):

            doll = board[row][col - 1]

            if doll > 0:
                board[row][col - 1] = 0

                if len(basket) > 0 and basket[-1] == doll:
                    basket.pop()
                    result += 2
                else:
                    basket.append(doll)
                break

    return result


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4])
      )
