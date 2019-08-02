'''
다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

입력
89, 90, 100

출력
국어, 영어, 수학의 총점: 279
'''

class Student:

    def __init__(self,scores_str):
        scores = scores_str.split(",")
        scores_strip = [int(num) for num in scores]

        self.kor = scores_strip[0]
        self.eng = scores_strip[1]
        self.math = scores_strip[2]

    def get_sum(self):
        return self.kor + self.eng + self.math

input_score = input()

s1 = Student(input_score)

print("국어, 영어, 수학의 총점: {}".format(s1.get_sum()))