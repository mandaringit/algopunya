case_number = int(input())

# 테스트 개수
for loop_number in range(case_number):
    N, M = (int(num) for num in input().split())
    fly_zone = []

    # N * N 배열 만들기
    for i in range(N):
        fly_list = [int(num) for num in input().split()]
        fly_zone.append(fly_list)

    # fly_zone 에서 M * M 만큼선택하기
    limit_length = N-M+1

    # 최고 킬
    most_kill = 0

    for i in range(limit_length):
        for j in range(limit_length):
            # 기준점 선정 => i,j

            total_kill = 0

            # 기준점에서 M * M 넓이의 죽인 수 구하기
            for kill_width in range(i, i+M):
                for kill_height in range(j, j+M):
                    total_kill += fly_zone[kill_width][kill_height]

            # 크기 비교하면서 most_kill 선택
            if most_kill < total_kill:
                most_kill = total_kill
    print(f"#{loop_number+1} {most_kill}")


# 테스트 끄적
"""
area = 5
kill = 2

zone = [
    [1,3,3,6,7],
    [8,13,9,12,8],
    [4,16,11,12,6],
    [2,4,1,23,2],
    [9,13,4,7,3]
]

# area_width = 5 일때, 최소 (0,0)
print(zone[0][0])
# 최대 (M-1,M-1)까지
print(zone[4][4])

# kill =2 일때, 가로/세로는 0 ~ 1 / 1 ~ 2 / 2 ~ 3 .. 이런식으로 증가하고(i + kill -1),, 
# area - kill= 3 까지 밖에 못감

# zone 에서 kill * kill 만큼선택하기
limit_length = area-kill+1

most_kill = 0
for i in range(limit_length):
    for j in range(limit_length):
#         kill_1 = zone[i][j]
#         kill_2 = zone[i][j+1]
#         kill_3 = zone[i+1][j]
#         kill_4 = zone[i+1][j+1]
#         total_kill = kill_1 + kill_2 + kill_3 + kill_4

        total_kill = 0
        
        for kill_width in range(i,i+kill):
            for kill_height in range(j,j+kill):
                total_kill += zone[kill_width][kill_height]
        

        print(f"({i},{j})기준 넓이 => {total_kill}")
        if most_kill < total_kill:
            most_kill = total_kill
            
print(most_kill)
"""

"""
N,M = (6,3)
fly_zone = [
 [29, 21 ,26, 9, 5, 8],
[21 ,19, 8 ,0 ,21 ,19],
[9 ,24, 2 ,11, 4, 24],
[19, 29, 1, 0, 21 ,19],
[10 ,29, 6 ,18 ,4 ,3],
[29 ,11 ,15 ,3 ,3 ,29]
]

# N * N 배열 만들기
for i in range(N):
#     fly_list = [int(num) for num in input().split()]
#     fly_zone.append(fly_list)

    # fly_zone 에서 M * M 만큼선택하기
    limit_length = N-M+1

    #최고 킬
    most_kill = 0

for i in range(limit_length):
    for j in range(limit_length):
        # 기준점 선정 => i,j

        total_kill = 0

        # 기준점에서 M * M 넓이의 죽인 수 구하기
        for kill_width in range(i,i+M):
            for kill_height in range(j,j+M):
                print(kill_width,kill_height)
                total_kill += fly_zone[kill_width][kill_height]
                
        print(f"({i},{j})기준 넓이 => {total_kill}")
        # 크기 비교하면서 most_kill 선택
        if most_kill < total_kill:
            most_kill = total_kill
print(f"#{loop_number+1} {most_kill}")
"""
