import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    gaps = set()

    fun_days = [int(input()) for _ in range(N)]

    for day in fun_days[1:]:

        if gaps:
            is_gap_exist = False
            for gap in gaps:
                if day % gap == 1:
                    is_gap_exist = True
                    break

            if not is_gap_exist:
                gaps.add(day - 1)

        else:
            gaps.add(day - 1)

    print("#{} {}".format(tc, len(gaps)))
