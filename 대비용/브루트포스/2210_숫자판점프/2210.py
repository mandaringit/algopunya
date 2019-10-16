import sys

sys.stdin = open('input.txt', 'r')

# 상대적으로 배열의 크기가 5*5로 고정이여서 모두 탐색해도 시간이 오래 걸리지 않는다.
# 브루트포스 + BFS/DFS 조합.

def DFS(i, j):
    global cases
    global board
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = [(i, j, 1, str(board[i][j]))]

    while stack:
        i_, j_, count, path = stack.pop()

        if count == 6:
            cases.add(path)
        else:
            for dx, dy in d:
                ni = i_ + dx
                nj = j_ + dy

                if 0 <= ni < 5 and 0 <= nj < 5:
                    stack.append((ni, nj, count + 1, path + str(board[ni][nj])))


board = [list(map(int, input().split())) for _ in range(5)]  # 무조건 5*5
cases = set()

for i in range(5):
    for j in range(5):
        DFS(i, j)

print(len(cases))
