'''
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
'''

str = input()

split_str = str.split(',')

make_list = [int(number.strip()) for number in split_str]
make_tuple = tuple(make_list)

print(make_list)
print(make_tuple)