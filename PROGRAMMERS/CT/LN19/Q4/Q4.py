import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
seats = ''.join(input().strip().split())
possible_seats = seats.split('1')

seat_count = 0
seat_idx = 0

for i in range(len(possible_seats)):
    length = len(possible_seats[i])
    if length > seat_count:
        seat_count = length
        seat_idx = i

distance = 0

# 중간에 껴있을때
if 0 < seat_idx < len(possible_seats) - 1:
    distance = seat_count // 2 + 1
elif seat_idx == 0 or seat_idx == len(possible_seats) - 1:  # 어느한쪽 옆에 누군가 없을때
    distance = seat_count

print(distance)
