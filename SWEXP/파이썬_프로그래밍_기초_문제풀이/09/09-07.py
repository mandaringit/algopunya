'''
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해


짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는


프로그램을 작성하십시오.
'''

lists = list(range(1,11))

even_list = list(filter(lambda x:x%2 ==0,lists))
even_and_square_list = list(map(lambda x:pow(x,2),even_list))

print(even_and_square_list)