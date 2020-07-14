count = int(input())
for i in range(count):
    star = " "*(count-(i+1)) + "*"*(i+1)
    print(star)
