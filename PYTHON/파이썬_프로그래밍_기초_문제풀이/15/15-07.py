"""
Person를 부모 클래스로 Male, Female 자식 클래스를 정의하는 코드를 작성하십시오.

"Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는

"Male", "Female" 값을 반환하는 메서드로 오버라이딩합니다.
"""


class Person:

    def getGender(self):
        return "Unknown"


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):

    def getGender(self):
        return "Female"


man = Male()
girl = Female()

print(man.getGender())
print(girl.getGender())
