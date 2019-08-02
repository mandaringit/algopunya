# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
#
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

operend = int(input("양의 정수를 입력하세요 : "))
count = 0

for i in range(1,operend+1):
    if operend%i == 0:
        count += 1
        print("%d(은)는 %d의 약수입니다." %(i,operend))

if count == 2:
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." %(operend,operend))