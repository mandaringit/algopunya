'''
한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다.

이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다.

다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.
'''

student1 = (90,80)
student2 = (85,75)
student3 = (90,100)

students = [student1,student2,student3]

for idx,scores in enumerate(students):
    total_score = scores[0]+scores[1]
    avg = total_score/len(scores)
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(idx+1,total_score,avg))