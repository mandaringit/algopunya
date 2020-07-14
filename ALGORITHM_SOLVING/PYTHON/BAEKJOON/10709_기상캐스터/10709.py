import sys

sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]

empty_sky = [[-1] * W for _ in range(H)]
for i in range(H):
    for j in range(W):

        if sky[i][j] == 'c':
            empty_sky[i][j] = 0
            how_far = 0
            ni = i
            nj = j + 1
            while 0 <= ni < H and 0 <= nj < W:
                how_far += 1
                if sky[ni][nj] == '.':
                    empty_sky[ni][nj] = how_far
                    nj += 1
                else:
                    break

for row in empty_sky:
    print(' '.join(map(str, row)))
