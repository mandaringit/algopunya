# 2292 벌집
# 모양은 중요하지 않다. 몇번째 겹이냐가 중요하다.
# 중앙에서 시작하므로 어디든 결과는 동일하기 때문이다.
# 각 겹에 몇번이 들어가느냐를 구해야 한다.

# 0번째 => [1] => range(1,2)
# 1번째 => [2 ~ 7] 6개 + => range(2,8)
# 2번째 => [8 ~ 19] 12개 + => range(8,20)
# 3번째 => [20 ~ 37] 18개 + ... => range(20,38)

# 그러므로 예로, 1부터 13까지는 0 -> 2번째 겹까지 시작과 끝을 포함하니까 0,1,2 로 3개를 지난다.
# 1부터 58 까지는 0 -> 4번째 겹까지, 0,1,2,3,4 로 5개를 지난다.

N = int(input())

floor = 0
gap = 1
floor_start = 1
floor_end = floor_start + gap
while N not in range(floor_start, floor_end):
    print(floor, gap, floor_start, floor_end)
    floor += 1
    floor_start = floor_end
    gap = floor * 6
    floor_end = floor_start + gap

print(floor+1)
