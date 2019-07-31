A = int(input())
B = int(input())
C = int(input())

result = A*B*C

for i in range(0, 10):
    print(str(result).count(str(i)))
