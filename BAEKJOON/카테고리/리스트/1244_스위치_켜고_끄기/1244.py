import sys

sys.stdin = open('input.txt', 'r')

switch_count = int(input())

switches = list(map(int, input().split()))

student_count = int(input())

for _ in range(student_count):
    # 남 1 여 2
    gender, switch_number = map(int, input().split())

    idx = switch_number - 1
    # 남자일때
    if gender == 1:

        while idx < switch_count:
            switches[idx] = 0 if switches[idx] else 1

            idx += switch_number

    # 여자일때
    else:
        # 자기 자신은 바꾸고,

        switches[idx] = 0 if switches[idx] else 1

        l_idx = idx - 1
        r_idx = idx + 1

        # 대칭을 살핀다.
        while l_idx >= 0 and r_idx < switch_count:

            left = switches[l_idx]
            right = switches[r_idx]

            # 둘이 동일하면 바꾸고
            if left == right:
                switches[l_idx] = 0 if switches[l_idx] else 1
                switches[r_idx] = 0 if switches[r_idx] else 1

                l_idx -= 1
                r_idx += 1
            else:
                # 아니면 탈출
                break

start = 0
last = 20

while start < switch_count:
    print(f"{' '.join(map(str,switches[start:last]))}")

    start += 20
    last += 20
