# for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

'''
    *
   **
  ***
 ****
*****
'''

starLen = 5

for i in range(1, starLen+1):
    print(" " * (starLen - i) + "*" * i)