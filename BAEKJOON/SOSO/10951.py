# EOF를 알아보세요
import sys

while True:
    nums = sys.stdin.readline()
    if nums == "":
        break
    a, b = tuple(map(int, nums.split()))
    print(a+b)
