import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    schedules = [tuple(map(int, input().split())) for _ in range(N)]

    schedules.sort(key=lambda x: x[1])  # 종료시간으로 정렬

    result_schedules = [schedules[0]]
    for start, end in schedules[1:]:

        prev_schedule = result_schedules[-1]
        prev_end = prev_schedule[1]

        if start < prev_end <= end:
            pass
        else:
            result_schedules.append((start, end))

    print("#{} {}".format(tc, len(result_schedules)))
