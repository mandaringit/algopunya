class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{}(name: {} gender: {} height: {})".format(self.__class__.__name__, self.name, self.gender, self.height)


students = [
    Student("홍길동", "남", 176.5),
    Student("홍길순", "여", 167.5),
    Student("김혁준", "남", 156.5),
    Student("김다정", "여", 146.5)
]

for student in students:
    print(student)

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
    print(student)

print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
    print(student)

print("height으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)
