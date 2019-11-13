import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
mindiff = 100*N*N
for x in range(0, N-2):
    for y in range(1, N-1):
        # d1 => ld length 1 ~ y 까지 가능
        # d2 => rd length 1 ~ N - y 까지 가능
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                points = [(x, y), (x+d1, y-d1), (x+d2, y+d2), (x+d1+d2, y-d1+d2)]

                is_okay = True
                for x_, y_ in points:
                    if 0 <= x_ < N and 0 <= y_ < N:
                        pass
                    else:
                        is_okay = False

                # 모든 꼭지점이 범위에 들어가면 그때 시작
                if is_okay:
                    areas = [0, 0, 0, 0, 0]  # 차례대로 1,2,3,4,5 구역 넓이

                    # 1~ 4구역 너비 (5구역 제외 전)
                    for i in range(N):
                        for j in range(N):
                            if 0 <= i < x+d1 and 0 <= j < y+1:
                                visited[i][j] = 1

                            elif 0 <= i < x+d1 and y+1 <= j < N:
                                visited[i][j] = 2

                            elif x+d1 <= i < N and 0 <= j < y+1:
                                visited[i][j] = 3

                            elif x+d1 <= i < N and y+1 <= j < N:
                                visited[i][j] = 4
                    print(visited)
print(mindiff)
