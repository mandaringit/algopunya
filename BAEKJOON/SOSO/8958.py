T = int(input())

for _ in range(T):
    Q = input()
    total = 0
    stack = 0
    for result in Q:
        if result == 'O':
            stack += 1
            total += stack
        else:
            stack = 0
    print(total)
