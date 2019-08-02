'''
주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.
'''

sample_tuple = (1,2,3,4,5,6,7,8,9,10)

half = int(len(sample_tuple)/2)

print(sample_tuple[:half])
print(sample_tuple[half:])