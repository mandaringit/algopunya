'''
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

** 못품 ** 어케풀어
'''

fibonacci = [1,1]

for i in range(0,10 - len(fibonacci)):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])

print(fibonacci)