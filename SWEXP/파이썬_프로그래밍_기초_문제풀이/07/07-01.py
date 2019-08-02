'''
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,

60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
'''

studentesScore = [88,30,61,55,95]
cnt = 1

for i in studentesScore:
    if i >= 60 :
        print("%d번 학생은 %d점으로 합격입니다." %(cnt,i))
    else :
        print("%d번 학생은 %d점으로 불합격입니다." % (cnt, i))
    cnt += 1