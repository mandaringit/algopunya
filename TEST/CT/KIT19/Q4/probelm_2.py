import sys

sys.stdin = open('input.txt', 'r')

"""
방은 1번부터 k까지 있으며
사람들은 원하는 방을 선택할 수 있다.
방이 비어있다면 그 방에 바로 배정 받을 수 있고
방이 비어있지 않다면 해당 방의 번호보다 크면서 비어있는 가장 작은 방에 할당된다.

전체 방의 수 k가 주어지고
사람들이 원하는 방 번호가 순서대로 들어가있는 배열이 주어질때
사람들이 할당받는 방의 번호를 순서대로 배열에 담아 출력하라

방의 수 k는 최대 10^12까지 주어 질 수있다.
올 수 있는 투숙객은 최대 200,000 ?
"""

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
