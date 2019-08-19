case = int(input())

for case_count in range(case):

    move = int(input())
    V = 0
    distance = 0

    for command_count in range(move):
        command = list(map(int, input().split()))
        if command[0] == 1:
            a = command[1]
            V += a
        elif command[0] == 2 and V > 0:
            a = command[1]
            V -= a
            if V <= 0:
                V = 0

        distance += V

    print(f"#{case_count + 1} {distance}")
