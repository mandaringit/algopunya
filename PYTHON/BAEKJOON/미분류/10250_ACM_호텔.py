# 잘 안떠오르면 그림을 그려라 멍충아
T = int(input())

for _ in range(T):
    H, W, N = tuple(map(int, input().split()))

    room = N // H + 1  # 몫 : 호수
    floor = N % H  # 나머지 : 층수

    # 나머지 == 0이면,
    if floor == 0:
        # 몫이 호수가 되고,
        room = N // H
        # 층수는 최상층이 된다.
        floor = H

    user_room_len = len(str(room))
    if user_room_len == 1:
        room = "0" + str(room)
    print(f"{floor}{room}")

"""
# 10250 ACM 호텔

# 무조건 가까운게 장땡

# 왼쪽부터 차곡차곡 채운다.


H = 1 # 층수
W = 99 # 길이
N = 99 # 번째 손님

# 호수에 0 붙이기 위한 작업
for i in range(1,H*W+1):
    N = i
    
    room = N // H +1 #  몫 : 호수
    floor = N % H # 나머지 : 층수 
    
    # 나머지 == 0이면,
    if floor == 0:
        # 몫이 호수가 되고,
        room = N // H
        # 층수는 최상층이 된다.
        floor = H
    
        
    user_room_len = len(str(room))
    if user_room_len == 1:
        room = "0" + str(room)

    print(f"{floor}{room}",end =" ")
"""
