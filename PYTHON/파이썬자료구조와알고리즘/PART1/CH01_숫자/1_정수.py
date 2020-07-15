# 정수의 바이트수 확인
print((999).bit_length())  # 10

# 정수 변환, 진법 변환
s = '11'
d = int(s)
print("문자열('11') -> int", d)

b = int(s, 2)
print("s -> b:", b)
