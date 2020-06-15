t1 = 1234, '안녕!'
print(t1[0])
print(t1)

x, *y = (1, 2, 3, 4)
print(x, y)

# 네임드 튜플 => 튜플 항목을 인덱스 뿐만 아니라 이름으로도 참조 가능!
import collections

Person = collections.namedtuple('Person', 'name age gender')
# Person = collections.namedtuple('Person', ['name', 'age', 'gender'])
# Person = collections.namedtuple('Person', ('name', 'age', 'gender'))
p = Person('아스틴', 30, '남자')
print(p)
print(p[0])
print(p.name)
p.age = 20 # 에러!
