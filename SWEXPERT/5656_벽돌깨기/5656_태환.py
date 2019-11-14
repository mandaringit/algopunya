def shoot(w_loc, shot, cnt, block):
    global N, W, H, min_break, all_block
    if min_break == 0:
        return
    if cnt >= all_block:
        min_break = 0
        return
    if shot <= 0:
        if min_break > all_block-cnt:
            min_break = all_block-cnt

        return
    q = [0]*(W*H+1)
    visit = [[0]*W for _ in range(H)]
    f = r = -1
    chk = 0
    for i in range(H):
        if block[i][w_loc] != 0:
            shot -= 1
            r += 1
            q[r] = [i, w_loc]
            visit[i][w_loc] = 1
            if block[i][w_loc] > 1:
                break
            else:
                if shot == 0:
                    break
                f += 1
    else:
        if r == -1:
            return

    while f != r:
        f += 1
        i, j = q[f]
        range_b = block[i][j]

        for m in range(1, range_b):
            for k in range(4):
                ni = i+d[k][0]*m
                nj = j+d[k][1]*m
                if 0 <= ni < H and 0 <= nj < W and visit[ni][nj] == 0 and block[ni][nj]:
                    r += 1
                    q[r] = [ni, nj]
                    visit[ni][nj] = 1

    q = q[0: r+1]
    q.sort(key=lambda x: x[0])
    for k in range(r+1):
        i, j = q[k]
        for m in range(i, -1, -1):
            if m != 0:
                block[m][j] = block[m-1][j]
            else:
                block[m][j] = 0

    for tt in range(W):
        block2 = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                block2[i][j] = block[i][j]

        shoot(tt, shot, cnt+r+1, block2)


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())+1
for tc in range(1, T):
    N, W, H = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(H)]
    all_block = 0
    for i in range(H):
        for j in range(W):
            if li[i][j]:
                all_block += 1
    min_break = all_block
    for i in range(W):
        block = [[0]*W for _ in range(H)]
        for j in range(H):
            for k in range(W):
                block[j][k] = li[j][k]
        shoot(i, N, 0, block)

    print('#{0} {1}'.format(tc, min_break))