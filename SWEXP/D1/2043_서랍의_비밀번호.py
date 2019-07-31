# 항상 P가 K보다 크다고 가정하는듯하다
pwd, pick = (int(pwd) for pwd in input().split())
cnt = 0
while pwd+1 != pick:
    pick += 1
    cnt += 1
print(cnt)
