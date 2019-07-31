H, M = tuple(map(int, input().split()))

if M > 45:
    print(H, M-45)
else:
    H = 23 if H-1 < 0 else H-1
    print(H, 15+M)
