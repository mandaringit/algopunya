# 3
# 540ms
T = int(input())

results = []

for t in range(1, T+1):
    N, Q = map(int, input().split())

    boxes = [0]*N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for box_num in range(L-1, R):
            boxes[box_num] = i

    results.append(f"#{t} {' '.join(map(str,boxes))}")

print("\n".join(results))


# 2
# 751ms
"""
T = int(input())

for t in range(1,T+1):
    N,Q = map(int,input().split())
    
    boxes = [0]*N
    
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for box_num in range(L-1,R):
            boxes[box_num] = i
    
    print(f"#{t}" ,end=" ")
    for i in boxes:
        print(f"{i}",end=" ")
    print()
"""


# 1
# 1806ms
"""
T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    boxes = ["0"]*N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for box_num in range(L-1, R):
            boxes[box_num] = str(i)

    print(f"#{t} {' '.join(boxes)}")
"""
