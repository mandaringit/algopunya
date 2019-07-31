N = int(input())  # => [4,1]

line = 1
next_num = 1

while N > next_num:
    line += 1
    next_num += line

line_start = next_num - line + 1
gap = N - line_start

if line % 2 == 0:
    i = 1 + gap
    j = line - gap
else:
    i = line - gap
    j = 1 + gap

print(f"{i}/{j}")

"""
#1193 분수찾기
# 대각선의 길이는 1 -> 2 -> 3 -> 4 -> .. 이렇게 커진다.

# X번째 [i,j]를 구해야 한다.

# 먼저 X가 몇번째 대각선 안인지 구한다.
# 대각선 이 K번째라고 치면,

N = 14 # => [4,1]

total = 0
K = 1

while True:
    total += K
    if 1<= N <= total:
        break
    K +=1
    
print(total)
print(f"몇번째 대각선 ? => {K}번째")

#이제 이 대각선에서 N이 몇번째인지 찾아야 한다.
# 보통 시작은 total - K +1 번째.

start = total - K + 1

# 찾을 수와 대각선 첫번째와의 간격

gap = N - start
print(f"갭 => {gap}")

# 대각선이 홀수번째인지 짝수번째인지 구한다
# 홀수 대각선은 K부터 1씩 i가 감소하고 j는 1부터 K까지 1씩 증가하는 방향으로 진행된다.
# 짝수 대각선은 i가 증가하고 j는 감소하는 방향으로 진행된다. 반대로 보면 된다.

# 그 대각선의 시작부터 i,j를 규칙에 따라 증가,감소 시키면서 해당 장소까지 가면 끝.

i = j = 0

# 짝수
if K % 2 == 0 :
    i = 1 + gap
    j = K - gap
# 홀수
else:
    i = K - gap
    j = 1 + gap

print(f"{i}/{j}")
"""
