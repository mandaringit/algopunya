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
            i = number
            while i in assigned_rooms:
                i += 1

            rooms[i] += 1
            assigned_rooms.append(i)

    return assigned_rooms


solution(10, [1, 3, 4, 1, 3, 1])
