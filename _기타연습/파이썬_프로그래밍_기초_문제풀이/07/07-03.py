# 1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.

# 2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100

result = ""
isFirst = True

for i in range(1,101):
    if i%2 == 0 :
        if isFirst:
            result += "%d" % i
            isFirst = False
        else :
            result += " %d" % i

print(result)