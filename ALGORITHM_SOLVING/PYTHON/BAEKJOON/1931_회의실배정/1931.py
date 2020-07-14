import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

schedules = [tuple(map(int, input().split())) for _ in range(N)]

schedules.sort()  # *시작 시간 먼저 정렬해줄 필요 있음 ->(3,4) 이후  (8,8), (5,8), (8,8) 이렇게 되면 (5,8)을 넣지 않을 수 있기 때문
schedules.sort(key=lambda x: x[1])  # 그다음 끝나는 시간으로 정렬

result_schedules = [schedules[0]]

for start, end in schedules[1:]:

    prev_schedule = result_schedules[-1]

    prev_end = prev_schedule[1]

    if start < prev_end <= end:
        pass
    else:
        result_schedules.append((start, end))

print(len(result_schedules))  # 6
