operend = int(input("양의 정수를 입력하세요 : "))

for i in range(1,operend+1):
    if operend%i == 0:
        print("%d(은)는 %d의 약수입니다." %(i,operend))