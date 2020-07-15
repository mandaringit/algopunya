import sys

sys.stdin = open('input.txt', 'r')

# 효율성 ..
def solution(k, room_number):
    rooms = [0] * (k + 1)
    assigned_rooms = []
    for number in room_number:
        if rooms[number] == 0:
            rooms[number] += 1
            assigned_rooms.append(number)
        else:
            for n_num in range(number + 1, k + 1):
                if rooms[n_num] == 0:
                    rooms[n_num] += 1
                    assigned_rooms.append(n_num)
                    break

    return assigned_rooms

