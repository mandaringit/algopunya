T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())  # 수강생수 N ,제출자수 K

    students = [i for i in range(1, N+1)]

    assignments = list(map(int, input().split()))

    for done in assignments:
        students.remove(done)

    print(f"#{t} {' '.join(map(str,students))}")
