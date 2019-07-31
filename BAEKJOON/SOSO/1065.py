# 양의 정수 X의 각 자리수가 등차 수열(연속된 두개의 수의 차이가 일정)을 이룬다? => 한수
def hansu(n):
    if 0 < n < 10:
        return True
    else:
        snum = str(n)
        gap = int(snum[0]) - int(snum[1])

        i = 1
        while True:
            if i == len(snum)-1:
                break
            new_gap = int(snum[i]) - int(snum[i+1])
            if new_gap != gap:
                return False
            i += 1
        return True


number = int(input())
count = 0
for i in range(1, number+1):
    if hansu(i):
        count += 1
print(count)
