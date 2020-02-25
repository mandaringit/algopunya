# 셀프 넘버 => 생성자가 없는 숫자

# n을 d(n)의 생성자라 한다.


def d(n):
    str_num = str(n)
    total = 0
    for i in str_num:
        total += int(i)
    return n + total


number_set = set()

i = 1
while True:
    if i > 10000:
        break
    number_set.add(d(i))
    i += 1

for number in range(1, 10001):
    if number not in number_set:
        print(number)
