# 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

# 1, 3, 5, 7, 9, ... 95, 97, 99

result = ""
isFirst = True

for i in range(1,101):
    if i % 2 != 0:
        if isFirst:
            result += "%d" % i
            isFirst = False
        else :
            result += ", %d" % i

print(result)