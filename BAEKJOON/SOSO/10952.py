while True:
    a, b = tuple(map(int, input().split()))
    if not a and not b:
        break
    print(a+b)
