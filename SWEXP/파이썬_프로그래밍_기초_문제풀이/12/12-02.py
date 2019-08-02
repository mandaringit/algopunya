'''
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.

'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
'''

str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
moeum = 'aeiou'
strList = list(str)
remove_aeiou = [x for x in strList if x not in moeum]

result = ''
for char in remove_aeiou:
    result += char
print(result)