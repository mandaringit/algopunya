# 단일케이스

floor = int(floor)

odd_num = 1

last_floor = []

for i in range(1, floor+1):
    for _ in range(1, i*2):
        if i == floor:
            last_floor.append(odd_num)
        odd_num += 2

print(f"{last_floor[0]} {last_floor[-1]}")
