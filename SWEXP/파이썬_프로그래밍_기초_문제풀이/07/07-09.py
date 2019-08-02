# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
"""
*******
 *****
  ***
   *
"""

# i = 7
# while i > 0:
#     print("{0:^7}".format("*"*i))
#     i -= 2

i = 0
j = 7
while i < 4 :
    while j > 0 :
        print(" "* i + "*" * j)
        i += 1
        j -= 2
