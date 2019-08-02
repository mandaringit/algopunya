'''
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와

같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된

알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
'''

str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

sum = 0
for alphabet in str:
    if alphabet == "A":
        sum += 4
    elif alphabet == "B" :
        sum += 3
    elif alphabet == "C" :
        sum += 2
    else :
        sum += 1
print(sum)


# map_list = list(map(lambda x: ,list(str)))

# print(map_list)