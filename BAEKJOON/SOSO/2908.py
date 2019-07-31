num1, num2 = input().split()
rnum1 = int(num1[::-1])
rnum2 = int(num2[::-1])
print(rnum1) if rnum1 > rnum2 else print(rnum2)
