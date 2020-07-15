# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
# 입력 : 9
# 출력 : 1001

decimal = int(input())

result = ""

while decimal > 0:
    q = decimal // 2
    r = decimal % 2
    decimal = q
    result += str(r)

result = result[::-1]
print(int(result))