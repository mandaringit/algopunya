import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
testers = list(map(int, input().split()))
B, C = map(int, input().split())

director_count = 0

for tester in testers:
    count = 1  # 총감독관 무조건 한명 포함
    if tester - B > 0:  # 분자가 음수가 되는 경우 방지
        include_as, rest = divmod(tester - B, C)
        count += include_as
        if rest > 0:
            count += 1

    director_count += count
print(director_count)
